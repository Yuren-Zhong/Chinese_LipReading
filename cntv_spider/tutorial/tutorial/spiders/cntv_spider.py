# coding: utf8

import scrapy
from os.path import join
from urllib import urlopen
from lib.cntv import get_download_link
import os
import subprocess
import time
import datetime

index = 60000

def download(url):
    global index

    html_f = urlopen(url)
    html_content = html_f.read()
    html_f.close()

    try:
        _, rest = html_content.split('<title>')
        title, _ = rest.split('</title>')

        _, rest = html_content.split(u'央视网消息'.encode('gbk'))
        script, _ = rest.split('<!--end content body-->')

        title = title.decode('gbk').encode('utf-8')
        script = script.decode('gbk').encode('utf-8')

        cmd = "python download_mp4.py --url " + url + " --index " + str(index) + " --path " + "new_videos"
        print('')
        print(cmd)

        timeout = 120
        delay = 10

        proc = subprocess.Popen(cmd)

        while proc.poll() is None and timeout > 0:

            time.sleep(delay)
            timeout -= delay

        if timeout <= 0:
            print("")
            print("timeout")
            proc.kill()

        with open(join('new_scripts', str(index)+'.txt'), 'w') as file:
            file.write(title)
            file.write('\n')
            file.write(script)

    except ValueError as e:
        try:
            os.remove(join('videos', str(index)+'.mp4'))
        except Exception:
            pass
        print (e)

    index += 1

class CNTVSpider(scrapy.Spider):
    name = "cntv"

    year = 2010
    month = 8
    day = 25

    def start_requests(self):  
        urls = list()
        date_int = self.date2int()
        if date_int < 20090625:
            pass
        elif date_int < 20100506:
            urls.append("http://news.cctv.com/program/xwlb/" + self.date2str() + ".shtml")
        elif date_int < 20110406:
            urls.append("http://news.cntv.cn/program/xwlb/" + self.date2str() + ".shtml")
        elif date_int < 20130709:
            urls.append("http://cctv.cntv.cn/lm/xinwenlianbo/" + self.date2str() + ".shtml")
        elif date_int < 20160203:
            urls.append("http://cctv.cntv.cn/lm/xinwenlianbo/" + self.date2str() + ".shtml")
        else:
            urls.append("http://tv.cctv.com/lm/xwlb/day/" + self.date2str() + ".shtml")
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def date2int(self):
        return self.year * 10000 + self.month * 100 + self.day

    def date2str(self):
        y = str(self.year)
        if self.month < 10:
            m = '0' + str(self.month)
        else:
            m = str(self.month)
        if self.day < 10:
            d = '0' + str(self.day)
        else:
            d = str(self.day)
        return y + m + d

    def feb_days(self, year):
        if year % 4 != 0:
            return 28
        elif year % 400 != 0:
            return 29
        return 28

    def update_date(self):
        if self.day == 1:
            if self.month == 1:
                self.year -= 1
                self.month = 12
                self.day = 31
            else:
                self.month -= 1
                if self.month == 2:
                    self.day = self.feb_days(self.year)
                elif self.month in [1,3,5,7,8,10,12]:
                    self.day = 31
                else:
                    self.day = 30
        else:
            self.day -= 1

    def compose_next_page(self):
        date_int = self.date2int()
        if date_int < 20090625:
            return None
        elif date_int < 20100506:
            return "http://news.cctv.com/program/xwlb/" + self.date2str() + ".shtml"
        elif date_int < 20110406:
            return "http://news.cntv.cn/program/xwlb/" + self.date2str() + ".shtml"
        elif date_int < 20130709:
            return "http://cctv.cntv.cn/lm/xinwenlianbo/" + self.date2str() + ".shtml"
        elif date_int < 20160203:
            return "http://cctv.cntv.cn/lm/xinwenlianbo/" + self.date2str() + ".shtml"
        else:
            return "http://tv.cctv.com/lm/xwlb/day/" + self.date2str() + ".shtml"

    def parse(self, response):
        date_int = self.date2int()

        if date_int < 20090625:
            return

        print(datetime.datetime.now())

        # save html page
        filename = 'cntv-%s.html' % self.date2str()
        with open(join('pages', filename), 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        links = None
        # downloads videos and script
        if date_int < 20100506:
            try:
                links = response.css('div.md_bd div.title_list_box ul li a::attr(href)').extract()
            except Exception as e:
                links = None
        elif date_int < 20110406:
            try:
                links = response.css('div.md_bd div.title_list_box ul li a::attr(href)').extract()
            except Exception as e:
                links = None
        elif date_int < 20130709:
            try:
                links = response.css('div.md_bd div div.title_list_box_130503 ul li a::attr(href)').extract()
            except Exception as e:
                links = None
        elif date_int < 20160203:
            try:
                links = response.css('div.md_bd div div ul li a::attr(href)').extract()
            except Exception as e:
                links = None
        else:
            try:
                links = response.css('ul li a::attr(href)').extract()
            except Exception as e:
                links = None

        if links is not None:
            for url in links:
                download(url)

        # goto next page
        self.update_date()
        next_page_link = self.compose_next_page()
        if next_page_link is not None:
            yield response.follow(next_page_link, callback=self.parse)