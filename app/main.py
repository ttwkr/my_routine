import time
import datetime
import asyncio
from fastapi import FastAPI

from app.config import settings

app = FastAPI()


async def count1(num: int):
    print(datetime.datetime.now())
    print(num)
    await asyncio.sleep(1)
    print("sleep")
    print(datetime.datetime.now())
    return num


async def count2(num: int):
    print(datetime.datetime.now())
    print(num)
    await asyncio.sleep(1)
    print("sleep2")
    print(datetime.datetime.now())
    return num


@app.get("/")
async def root():
    # await count1(1)
    # await count2(2)
    a = [count1(1), count2(2)]
    await asyncio.gather(*a)
    # await count1(1)
    # await count2(2)
    print('end')
    return {
        "info": {
            "DB": settings.RDS_DB,
            "HOST": settings.RDS_HOST
        }
    }
