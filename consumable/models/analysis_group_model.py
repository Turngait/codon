from app import Base
from sqlalchemy import Column, String, Text, Integer, DateTime
from datetime import datetime

class AnalysisGroup(Base):
  __tablename__ = 'analysis_groups'
  id = Column(Integer, primary_key = True)
  title = Column(String(length=150), nullable=False)
  description = Column(Text, nullable=True)
  user_id = Column(Integer, nullable=False)
  created_at = Column(DateTime, default=datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<Analyse %r>' % self.id
