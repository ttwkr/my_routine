from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models.members import Member

router = APIRouter()


@router.get('/')
async def get(db: Session = Depends(get_db)):
    members = db.query(Member).all()
    return members


@router.post('/')
async def save(db: Session = Depends(get_db)):
    """
    회원가입
    :param db: session
    :return:
    """
    pass


@router.post('login/')
async def login(db: Session = Depends(get_db)):
    """
    로그인
    :param db:
    :return:
    """
    pass


@router.post('login-out/')
async def login_out(db: Session = Depends(get_db)):
    """
    로그아웃
    :param db: session
    :return:
    """
    pass
