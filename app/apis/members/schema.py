from pydantic import BaseModel


class SendMail(BaseModel):
    email: str


class EmailVerificationSchema(BaseModel):
    email: str
    code: str
