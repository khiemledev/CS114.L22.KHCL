import scrapy


class HeadlinesSpider(scrapy.Spider):
    name = "theguardian"
    start_urls = [
        'https://www.theguardian.com/world/all'
    ]

    def parse(self, response):
        for headline in response.css('a.js-headline-text'):
            yield {
                'is_sarcastic': 0,
                'headline': headline.css('::text').get(),
                'article_link': headline.css('::attr("href")').get()
            }

        next_page = response.css('div.pagination__list a:last-child::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)