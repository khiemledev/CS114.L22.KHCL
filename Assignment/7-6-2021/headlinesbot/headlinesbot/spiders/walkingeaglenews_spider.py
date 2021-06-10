import scrapy


class HeadlinesSpider(scrapy.Spider):
    name = "walkingeaglenews"
    start_urls = [
        'http://walkingeaglenews.com/'
    ]

    def parse(self, response):
        for headline in response.css('h2.post-title'):
            yield {
                'is_sarcastic': 1,
                'headline': headline.css('a::text').get(),
                'article_link': headline.css('a::attr("href")').get()
            }

        next_page = response.css('div.nav-links a:last-child::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)