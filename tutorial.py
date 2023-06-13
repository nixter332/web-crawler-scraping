import scrapy

class Books(scrapy.Spider):
    name='spidey'
    start_urls=[
        "https://books.toscrape.com" 
    ]
    
    def parse(self,response):
        
            all_books=response.css('li .product_pod')
        
            title=all_books.css('article h3 a::text').extract()
            price=all_books.css('.price_color::text').extract()
            star_class=all_books.css('.star-rating').xpath("@class").extract()
            star=star_class[12:]
                
            yield{
                'title':title,
                'price':price,
                'rating':star
            }
            
            next_page=response.css('li.next a::attr(href)').get()
        
            if next_page is not None:
                yield response.follow(next_page,callback=self.parse)
