from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.apis.members.crud import Verification
from app.core.common import Common
from app.database.connection import get_db
from app.database.models.members import Member
from app.apis.members.schema import EmailVerification, SendMail

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


@router.post('/send-code')
async def send_code(data: SendMail, db: Session = Depends(get_db)):
    common = Common()
    # 코드생성
    code = common.rand_number_code()
    # 생성후 디비 저장
    # 이메일 전송
    return data


@router.post('/email-verify')
async def email_verify(data: EmailVerification, db: Session = Depends(get_db)):
    """
    이메일 인증
    :param data:
    :param db:
    :return:
    """
    return data


@router.post('/login/')
async def login(db: Session = Depends(get_db)):
    """
    로그인
    :param db:
    :return:
    """
    pass


@router.post('/login-out/')
async def login_out(db: Session = Depends(get_db)):
    """
    로그아웃
    :param db: session
    :return:
    """
    pass
