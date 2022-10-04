import platform
import sys

from fastapi import FastAPI

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()


@app.get("/")
async def read_root():
    message = ("Hello world! From FastAPI running on Uvicorn with Gunicorn. "
               f"Using Python {version} with platform {platform.uname()[4]}")
    return {"message": message}
