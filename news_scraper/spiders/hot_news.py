import scrapy


class HotNewsSpider(scrapy.Spider):
    name = 'hot_news'
    allowed_domains = ['www.inside.com.tw']
    start_urls = ['http://www.inside.com.tw/']

    def parse(self, response):

        post_urls = response.xpath(
            "//a[@class='hero_menu_link']/@href").getall()

        for post_url in post_urls:
            yield scrapy.Request(post_url, self.parse_content)

    def parse_content(self, response):

        # 熱門文章標題
        hot_news_title = response.xpath(
            "//h1[@class='post_header_title js-auto_break_title']/text()").get()

        # 熱門文章摘要
        hot_news_intro = response.xpath(
            "//div[@class='post_introduction']/text()").get()

        HotNewsItem = {
            "hot_news_title": hot_news_title,
            "hot_news_intro": hot_news_intro
        }

        return HotNewsItem
