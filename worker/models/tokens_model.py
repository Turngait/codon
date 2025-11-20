from sqlalchemy import String, Text, Integer, DateTime
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from datetime import datetime
from typing import List

class Base(DeclarativeBase):
  pass
class TokensModel(Base):
  __tablename__ = 'tokens'
  id: Mapped[int] = mapped_column(primary_key=True)
  token: Mapped[str] = mapped_column(Text, nullable=True)
  user_id: Mapped[int] = mapped_column(Integer, nullable=False)
  createdAt: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
  active_til: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<Tokens entity id = %r>' % (self.id)
