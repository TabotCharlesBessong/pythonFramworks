import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.css("article.product_pod").get()
        print(len(books))
        for book in books:
        # for i in range(1,21):
            yield {
                "name": response.css("article.product_pod h3 a::text").get(),
                "price": response.css(
                    "article.product_pod .product_price .price_color::text"
                ).get(),
                "url": response.css("article.product_pod h3 a").attrib["href"],
            }

        next_page = response.css("li.next a ::attr(href)").get()

        if next_page is not None:
            if "catalogue/" in next_page:
                next_page_url = "http://books.toscrape.com/" + next_page
            else:
                next_page_url = "http://books.toscrape.com/catalogue" + next_page
                
            yield response.follow(next_page_url,callback=self.parse)
