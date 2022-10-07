from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models.members import Member

router = APIRouter()


@router.get('/members/')
async def get_member(db: Session = Depends(get_db)):
    members = db.query(Member).all()

    return members
