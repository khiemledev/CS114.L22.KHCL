import scrapy


class HeadlinesSpider(scrapy.Spider):
    name = "theonion"
    start_urls = [
        'https://www.theonion.com/latest'
    ]

    def parse(self, response):
        for headline in response.css('div.aoiLP'):
            yield {
                'is_sarcastic': 1,
                'headline': headline.css('h2.eXwNRE::text').get(),
                'article_link': headline.css('a.js_link::attr("href")').get()
            }

        next_page = self.start_urls[0] + response.css('.sc-1uzyw0z-0 a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)