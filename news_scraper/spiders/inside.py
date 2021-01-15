import scrapy


class InsideSpider(scrapy.Spider):
    name = 'inside'
    allowed_domains = ['www.inside.com.tw']
    start_urls = ['https://www.inside.com.tw/tag/ai']

    def parse(self, response):
        title = response.xpath(
            "//a[@class='js-auto_break_title']/text()").get()

        print(title)
