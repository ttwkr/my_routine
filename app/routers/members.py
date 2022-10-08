import asyncio
import datetime

from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from app.apis.members.crud import EmailVerifications
from app.apis.members.module import Verification
from app.core.common import Common
from app.database.connection import get_db
from app.database.models.members import MemberModel, EmailVerificationModel
from app.apis.members.schema import EmailVerificationSchema, SendMail

router = APIRouter()


@router.get('/')
async def get(db: Session = Depends(get_db)):
    members = db.query(MemberModel).all()
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
async def send_code(data: SendMail, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    인증코드 전송
    :param background_tasks:
    :param data:
    :param db:
    :return:
    """
    common = Common()
    email_verify = EmailVerifications(db=db)
    ver = Verification()
    # 인증코드생성
    code = common.rand_number_code()
    # 생성후 디비 저장
    now = datetime.datetime.now()
    instance = EmailVerificationModel(email=data.email, code=code, expired_at=now)
    email_verify.save(instance=instance)
    # 이메일 전송
    # 오래 걸려 백그라운드 작업으로 돌림(비동기
    background_tasks.add_task(ver.send_mail, code, data.email)

    return data


@router.post('/email-verify')
async def email_verify(data: EmailVerificationSchema, db: Session = Depends(get_db)):
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
