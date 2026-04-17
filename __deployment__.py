"""Dave's runtime starter pack -- fruitshop ingest with a downstream ping."""

from fruitshop_pipeline import load_shop
from ping_job import ping

__all__ = ["load_shop", "ping"]
