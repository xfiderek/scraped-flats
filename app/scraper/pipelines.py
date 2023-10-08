from models import Flat
from database import SessionLocal


class ScraperPipeline:
    def __init__(self):
        self.db = SessionLocal()
        self.db.query(Flat).delete()

    def process_item(self, item, _):
        self.db.add(Flat(**item))

    def close_spider(self, _):
        self.db.commit()
        self.db.close()
