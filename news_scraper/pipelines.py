# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from news_scraper import settings
import pymysql
from scrapy.exporters import CsvItemExporter
from scrapy.mail import MailSender


class NewsScraperPipeline:

    def __init__(self):

        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DATABASE,
            user=settings.MYSQL_USERNAME,
            passwd=settings.MYSQL_PASSWORD,
            charset='utf8'
        )

        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        sql = 'INSERT INTO posts(post_title, post_date, post_author)VALUES(%s,%s,%s) '

        data = (item['post_title'], item['post_date'], item['post_author'])

        self.cursor.execute(sql, data)

        return item

    def close_spider(self, spider):
        self.connect.commit()
        self.connect.close()


class CsvPipeline:
    def __init__(self):
        self.file = open('posts.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='big5')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

        mail = MailSender(smtphost=settings.MAIL_HOST,
                          smtpport=settings.MAIL_PORT,
                          smtpuser=settings.MAIL_FROM,
                          smtppass=settings.MAIL_PASS,
                          smtptls=settings.MAIL_TLS)

        attach_name = "posts.csv"  # 附件的顯示名稱
        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        file_object = open("posts.csv", "rb")

        # 寄出郵件
        return mail.send(to=["example@gmail.com"],  # 收件者
                         subject="news",  # 郵件標題
                         body="",  # 郵件內容
                         attachs=[(attach_name, mime_type, file_object)])  # 附件
