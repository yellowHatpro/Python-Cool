# Basics of Scrapy
(A) Spider
> Structure

1. name: name of the spider
2. start_requests: returns an iterable of Request objects
3. parse: deals with the response downloaded for each of the requests made. This method usually parses the response , extracting the scraped data as dicts and also finding new URLs to follow and creating new requests (Reqeust) from them.

>Example of a spider
```
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
```