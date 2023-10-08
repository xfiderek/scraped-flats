# Scrapy settings for scraper project
BOT_NAME = "scraper"
SPIDER_MODULES = ["scraper"]
NEWSPIDER_MODULE = "scraper"
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
    "scraper.pipelines.ScraperPipeline": 300,
}
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
DEFAULT_REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
}
