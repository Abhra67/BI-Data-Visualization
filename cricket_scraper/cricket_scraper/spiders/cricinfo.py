import scrapy

class CricInfoSpider(scrapy.Spider):
    name = "cricinfo"
    start_urls = ["https://www.espncricinfo.com/series/world-cup"]  # World Cup page

    def parse(self, response):
        for match in response.css(".match-info"):
            yield {
                "match": match.css(".name::text").get(),
                "score": match.css(".score::text").get(),
                "status": match.css(".status-text::text").get(),
            }
