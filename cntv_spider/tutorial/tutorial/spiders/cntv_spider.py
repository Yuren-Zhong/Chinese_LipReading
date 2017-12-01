# coding: utf8

import scrapy
from os.path import join
from urllib import urlopen
from lib.cntv import get_download_link

index = 0

def download(url):
    global index
    get_download_link(url, target_filename=str(index)+'.mp4', quality_type=5, get_dlink_only=False, is_merge=False, is_remain=False)

    html_f = urlopen(url)
    html_content = html_f.read()

    _, rest = html_content.split(u'<strong>央视网消息</strong>（新闻联播）：'.encode('utf-8'))
    script, _ = rest.split('<!--repaste.body.end--></div>')

    with open(join('scripts', str(index)+'.txt'), 'w') as file:
        file.write(script)

    index += 1



class CNTVSpider(scrapy.Spider):
    name = "cntv"
    start_urls = [
        'http://search.cctv.com/ifsearch.php?qtext=%E6%96%B0%E9%97%BB%E8%81%94%E6%92%AD&type=video&page=1&datepid=1&vtime=0&channel=CCTV-1%E7%BB%BC%E5%90%88%E9%A2%91%E9%81%93&sort=',
    ]
    page_num = 1

    def parse(self, response):
        if self.page_num > 3:
            return

        # save html page
        page = response.url.split("/")[-2]
        filename = 'cntv-%s.html' % str(self.page_num)
        self.page_num += 1
        with open(join('pages', filename), 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        # downloads videos and script
        links = response.css('ul.list_rec li a.list_rec_video::attr(href)').extract()
        for link in links:
            _, rest = link.split('?targetpage=')
            url, _ = rest.split('&point=video_normal&')
            download(url)

        # goto next page
        page_links = response.css('div.seah_page div.ifpage a::attr(href)').extract()
        labels = response.css('div.seah_page div.ifpage a span').extract()
        next_page_link = None
        for i in range(len(labels)):
            if labels[i] == u'<span>\u4e0b\u4e00\u9875&gt;&gt;</span>':
                next_page_link = page_links[i-1]
                break
        if next_page_link is not None:
            yield response.follow(next_page_link, callback=self.parse)