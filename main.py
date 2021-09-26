from app import app

import uvicorn

__all__ = []

PORT = 5980


if __name__ == "__main__":
    uvicorn.run(
        app,
        port=5980
    )
