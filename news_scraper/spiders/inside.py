import scrapy


class InsideSpider(scrapy.Spider):
    name = 'inside'
    allowed_domains = ['www.inside.com.tw']
    start_urls = ['https://www.inside.com.tw/tag/ai']
    count = 1  # 執行次數

    def parse(self, response):

        yield from self.scrape(response)  # 爬取網頁內容

        # 定位「下一頁」按鈕元素
        next_page_url = response.xpath(
            "//a[@class='pagination_item pagination_item-next']/@href")

        if next_page_url:

            url = next_page_url.get()  # 取得下一頁的網址

            InsideSpider.count += 1

            if InsideSpider.count <= 3:
                yield scrapy.Request(url, callback=self.parse)  # 發送請求

    def scrape(self, response):

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
