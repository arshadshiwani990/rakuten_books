import scrapy


class RakutenSpider(scrapy.Spider):
    name = 'rakuten'
    allowed_domains = ['books.rakuten.co.jp']
    start_urls = ['http://books.rakuten.co.jp/']

    def parse(self, response):
        pass
