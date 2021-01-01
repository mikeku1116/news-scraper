import scrapy


class InsideSpider(scrapy.Spider):
    name = 'inside'
    allowed_domains = ['www.inside.com.tw']
    start_urls = ['http://www.inside.com.tw/']

    def parse(self, response):
        pass
