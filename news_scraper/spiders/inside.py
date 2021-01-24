import scrapy


class InsideSpider(scrapy.Spider):
    name = 'inside'
    allowed_domains = ['www.inside.com.tw']
    start_urls = ['https://www.inside.com.tw/tag/ai']

    def parse(self, response):

        # 爬取文章標題
        post_titles = response.xpath(
            "//h3[@class='post_title']/a[@class='js-auto_break_title']/text()"
        ).getall()

        # 爬取發佈日期
        post_dates = response.xpath(
            "//li[@class='post_date']/span/text()"
        ).getall()

        # 爬取作者
        post_authors = response.xpath(
            "//span[@class='post_author']/a/text()"
        ).getall()

        for data in zip(post_titles, post_dates, post_authors):
            NewsScraperItem = {
                "post_title": data[0],
                "post_date": data[1],
                "post_author": data[2]
            }
            yield NewsScraperItem
