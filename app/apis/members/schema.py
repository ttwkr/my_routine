from pydantic import BaseModel


class SendMail(BaseModel):
    email: str


class EmailVerification(BaseModel):
    code: str
