import scrapy


class InsideSpider(scrapy.Spider):
    name = 'inside'
    allowed_domains = ['www.inside.com.tw']
    start_urls = ['https://www.inside.com.tw/tag/ai']

    def parse(self, response):
        titles = response.css("a.js-auto_break_title::text").getall()

        for title in titles:
            print(title)
