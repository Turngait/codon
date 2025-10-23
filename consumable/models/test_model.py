from sqlalchemy import Column, String, Text, Integer

from app import Base
from datetime import datetime

class Tests(Base):
  __tablename__ = 'tests'
  id = Column(Integer, primary_key = True)
  title = Column(String(length=150), nullable=False)
  description = Column(Text, nullable=True)

  def __repr__(self):
    return '<Tests %r>' % self.id
