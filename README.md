# Chinese_LipReading

## Spider over CNTV website

### Environment Setup:
	```
	conda create -n cntv-spider python=2.7
	activate cntv-spider
	conda install -n cntv-spider scrapy curl
	pip install -n cntv-spider wget pycurl
	```

### Run:
	```
	cd cntv_spider\tutorial
	scrapy crawl cntv
	```

### NOTE:
	All the modifications should be in cntv_spider\tutorial\tutorial\spiders\cntv_spider.py, where the spider is implemented.

