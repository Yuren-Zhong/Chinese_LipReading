# Chinese Lip Reading

## Spider over CNTV website

### Environment Setup:
Anaconda should be installed first. I used Anaconda 4.3.30.
```	
conda create -n cntv-spider python=2.7
activate cntv-spider
conda install scrapy curl
pip install wget pycurl
```

### Run:
```
cd cntv_spider\tutorial
scrapy crawl cntv
```

### NOTE:
All the modifications should be in cntv_spider\tutorial\tutorial\spiders\cntv_spider.py, where the spider is implemented.

