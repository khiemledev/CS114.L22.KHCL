import scrapy


class HeadlinesSpider(scrapy.Spider):
    name = "huffpost"
    start_urls = [
        'https://www.huffpost.com/news/'
    ]

    def parse(self, response):
        for headline in response.css('div.card__headlines'):
            yield {
                'is_sarcastic': 0,
                'headline': headline.css('a.card__headline h2.card__headline__text::text').get(),
                'article_link': headline.css('a.card__headline::attr("href")').get()
            }

        next_page = response.css('ul.pagination li:last-child a.pagination__next-link::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)