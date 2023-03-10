from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


data = {
    "asin": "AMAZIN_ASIN_NUMBER",
    "title": "Mark 1"
}


class Product(Model):  # ---> Table
    __keyspace__ = "scraper_app"
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()
    price_str = columns.Text(default="80")


class ProductScrapeEvent(Model):
    __keyspace__ = "scraper_app"
    uuid = columns.UUID(primary_key=True)
    asin = columns.Text(index=True)
    title = columns.Text()
    price_str = columns.Text(default="80")


