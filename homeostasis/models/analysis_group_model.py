from sqlalchemy import String, Text, Integer, DateTime
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from datetime import datetime
from typing import List

class Base(DeclarativeBase):
  pass
class AnalysisGroupModel(Base):
  __tablename__ = 'analysis_groups'
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(length=150), nullable=False)
  description: Mapped[str] = mapped_column(Text, nullable=True)
  user_id: Mapped[int] = mapped_column(Integer, nullable=False)
  created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
  updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<AnalysisGroup entity id = %r, title = %s>' % (self.id, self.title)
