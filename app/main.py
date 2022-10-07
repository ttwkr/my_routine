import time
import datetime
import asyncio
from fastapi import FastAPI

from app.config import settings

app = FastAPI()


@app.get("/")
def root():
    return {
        "info": {
            "DB": settings.RDS_DB,
            "HOST": settings.RDS_HOST
        }
    }
