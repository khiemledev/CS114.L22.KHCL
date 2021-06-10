import scrapy


class HeadlinesSpider(scrapy.Spider):
    name = "thedailywtf"
    start_urls = [
        'https://thedailywtf.com/articles/2021/6'
    ]

    def parse(self, response):
        for headline in response.css('.article-content'):
            yield {
                'is_sarcastic': 1,
                'headline': headline.css('h2.title::text').get(),
                'article_link': headline.css('a.link-overlay::attr("href")').get()
            }

        next_page = response.css('div.series-nav div.prev a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)