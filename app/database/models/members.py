from sqlalchemy import Column, Integer, String, TIMESTAMP

from app.database.session import Base


class Member(Base):
    __tablename__ = "member"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)


class EmailVerification(Base):
    __tablename__ = "email_verification"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    code = Column(String)
    expired_at = Column(TIMESTAMP)
