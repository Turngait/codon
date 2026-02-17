from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Tests(Base):
  __tablename__ = 'tests'
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(length=150), nullable=False)
  description: Mapped[str] = mapped_column(Text, nullable=True)

  def __repr__(self):
    return '<Tests %r>' % self.id
