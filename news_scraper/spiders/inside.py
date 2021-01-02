import scrapy
import bs4


class InsideSpider(scrapy.Spider):
    name = 'inside'
    allowed_domains = ['www.inside.com.tw']
    start_urls = ['https://www.inside.com.tw/tag/ai']

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        titles = soup.find_all('h3', {'class': 'post_title'})
        for title in titles:
            print(title.text.strip())
