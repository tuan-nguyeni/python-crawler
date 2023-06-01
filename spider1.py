import scrapy


class QuoteSpider(scrapy.Spider):
     name = 'quote-spdier'
     start_urls = ['https://quotes.toscrape.com']

     def parse(self, response):
          QUOTE_SELECTOR = '.quote'
          TEXT_SELECTOR = '.text::text'
          AUTHOR_SELECTOR = '.author::text'

          for quote in response.css(QUOTE_SELECTOR):
               yield {
                    'text': quote.css(TEXT_SELECTOR).extract_first(),
                    'author': quote.css(AUTHOR_SELECTOR).extract_first(),
               }