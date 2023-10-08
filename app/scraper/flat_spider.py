import scrapy
from scrapy.spiders import CrawlSpider
import json


class FlatSpider(CrawlSpider):
    name = "flat"
    number_of_records = 500

    def start_requests(self):
        urls = [
            f"https://www.sreality.cz/api/en/v2/estates?category_main_cb=1&category_type_cb=1&per_page={self.number_of_records}"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        json_items = json.loads(response.body)
        for json_item in json_items["_embedded"]["estates"]:
            item = {}
            item["name"] = json_item["name"]

            images = json_item.get("_links", {}).get("images", [])
            if len(images) > 0:
                item["image_url"] = images[0]["href"]
            yield item
