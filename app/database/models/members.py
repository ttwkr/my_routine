from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import Session

from app.database.session import Base


class MemberModel(Base):
    __tablename__ = "member"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)


class EmailVerificationModel(Base):
    __tablename__ = "email_verification"

    id = Column(Integer, primary_key=True, index=True, )
    email = Column(String)
    code = Column(String)
    expired_at = Column(TIMESTAMP)

    def save(self, db: Session, instance):
        db.add(instance)
        db.commit()
