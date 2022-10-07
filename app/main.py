import time
import datetime
import asyncio
from fastapi import FastAPI

from app.config import settings
from app.routers import members

app = FastAPI()
app.include_router(members.router)


@app.get("/")
def root():
    return {
        "info": {
            "DB": settings.RDS_DB,
            "HOST": settings.RDS_HOST
        }
    }
