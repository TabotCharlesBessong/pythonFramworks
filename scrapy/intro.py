response  = fetch("http://books.toscrape.com/")
response
response.css("article.product_pod")
response.css("article.product_pod").get()
books = response.css("article.product_pod").get()
len(books)
book = books[0]
book.css("h3 a::text").get()
book.css("h3 a::text").get()
book.css(".product_price .price_color:::text").get()
books
book(".product_price .price_color:::text").get()
books
book1 = books("h3 a::text").get()
book2 = books[0]
book2
book3 = books[5]
book3
book4 = books[0][4]
response
response.css
books1 = response.css("article.product_pod h3 a::text").get()
books1
book_price = response.css("article.product_pod.product_price p::text").get()
book_price
book_price
book_price1 = response.css("article.product_pod.product_price p:::text").get()
book_price1 = response.css("article.product_pod.product_price p:::text").get()
book_price2 = response.css(
    "article.product_pod .product_price .price_color::text"
).get()
book_price2
# history
