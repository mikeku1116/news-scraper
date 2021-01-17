import scrapy


class InsideSpider(scrapy.Spider):
    name = 'inside'
    allowed_domains = ['www.inside.com.tw']
    start_urls = ['https://www.inside.com.tw/tag/ai']

    def parse(self, response):
        titles = response.xpath(
            "//div[@class='post_list_item_content']/h3[@class='post_title']/a/text()").getall()

        for title in titles:
            print(title)
