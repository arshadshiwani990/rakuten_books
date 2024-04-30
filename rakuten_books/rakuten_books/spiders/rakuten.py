import scrapy
import os

class RakutenSpider(scrapy.Spider):
    
    custom_settings = {
		"FEEDS": {
			os.path.join("scrapy_output", "rakuten.csv"): {
				"format": "csv",
				"overwrite": True,
			}
		},
		"ROBOTSTXT_OBEY": False,
		
	}
	
 
 
    name = 'rakuten'

    start_urls = ['https://books.rakuten.co.jp/search?g=001&e=1&o=0&l-id=search-c-pager']

    def parse(self, response):
        
        categories=response.xpath('//span[@class="rbcomp__aside__menu__item__current"]/following-sibling::ul/li/a/@href').extract()
        for category in categories:
            print(category)
            yield scrapy.Request(url=category, callback=self.parse)
            # break
        
        divs=response.xpath('//div[@class="rbcomp__item-list__item"]')
      
        for div in divs:
            isbn=div.xpath('.//p[@class="gbs"]')
            if isbn:
                isbn=isbn.xpath('.//@id').get().replace('ISBN','')
                print(isbn)     
                
                price=div.xpath('.//p[@class="rbcomp__price"]//em//text()').get().replace('円','')
                print(price) 

                
                item={}
                item['isbn']=isbn
                item['price']=price
                
                yield item
                
                print('------------------------')

        
        nextpage=response.xpath('//ul[@class="rbcomp__pager"]/following-sibling::div/a/@href').get()
        if nextpage:
            print(nextpage)
            yield scrapy.Request(url=nextpage, callback=self.parse)