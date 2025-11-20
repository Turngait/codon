from datetime import datetime
from sqlalchemy import String, Text, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase):
  pass

class UsersDataModel(Base):
  __tablename__ = 'data_of_users'
  id: Mapped[int] = mapped_column(primary_key=True)
  status: Mapped[int] = mapped_column(Integer, nullable=False)
  user_timezone: Mapped[str] = mapped_column(String(length=150), nullable=True)
  user_id: Mapped[int] = mapped_column(Integer, nullable=False)
  created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
  updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
  isBanned: Mapped[bool] = mapped_column(Boolean, default=False)
  biological_gender: Mapped[str] = mapped_column(String(length=1), nullable=False)
  data_birth: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
  weight: Mapped[int] = mapped_column(Integer, nullable=False)
  height: Mapped[int] = mapped_column(Integer, nullable=False)
  lang_interface: Mapped[str] = mapped_column(String(length=4), default="en")
  theme_interface: Mapped[str] = mapped_column(String(length=3), default="li")