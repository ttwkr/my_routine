from fastapi import FastAPI

from app.core.config import settings
from app.routers import members

# def create_app() -> FastAPI:
#     # 메인 앱실행
#     app = FastAPI()
#     # 라우터 추가
#     app.include_router(prefix='/members', router=members.router, tags=['members'])
#     return app


# app = create_app()
app = FastAPI()
app.include_router(prefix='/members', router=members.router, tags=['members'])


@app.get("/")
def root():
    return {
        "info": {
            "DB": settings.RDS_DB,
            "HOST": settings.RDS_HOST
        }
    }
