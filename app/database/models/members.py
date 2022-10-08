from sqlalchemy import Column, Integer, String

from app.database.session import Base


class Member(Base):
    __tablename__ = "member"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
