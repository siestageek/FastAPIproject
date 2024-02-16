from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from app.models.base import Base

class Member(Base):
    __tablename__ = 'member'

    mno = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(String(18), nullable=False, unique=True)
    passwd = Column(String(18), nullable=False)
    name = Column(String(10), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    regdate = Column(DateTime, default=datetime.now)







