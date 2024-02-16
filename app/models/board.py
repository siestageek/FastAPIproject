from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import mapped_column

from app.models.base import Base


class Board(Base):
    __tablename__ = 'board'

    bno = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(18), nullable=False)
    userid = mapped_column(String(18), ForeignKey('member.userid'))
    regdate = Column(DateTime, default=datetime.now)
    views = Column(Integer, default=0)
    contents = Column(Text, nullable=False)
