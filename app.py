import os

from fastapi import FastAPI
from fastapi_redis_cache import FastApiRedisCache

from src.routers import domain_router

REDIS_URL = "redis://redis:6379"

__all__ = [
    "app"
]

app = FastAPI()

app.add_route("/", domain_router)


@app.on_event("startup")
def startup():
    """Initialize Redis cache."""
    redis_url = os.environ.get("REDIS_URL", REDIS_URL)

    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=redis_url,
        prefix="cache",
    )
