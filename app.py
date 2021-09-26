from fastapi import FastAPI

from src.routers import domain_router

__all__ = [
    "app"
]

app = FastAPI()

app.add_route("/", domain_router)
