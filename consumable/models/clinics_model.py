from sqlalchemy import String, Text, Integer, DateTime, Boolean # pyright: ignore[reportMissingImports]
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column # pyright: ignore[reportMissingImports]
from datetime import datetime

class Base(DeclarativeBase):
  pass

class ClinicsModel(Base):
  __tablename__ = 'clinics'
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(length=150), nullable=False)
  description: Mapped[str] = mapped_column(Text, nullable=True)
  main_site: Mapped[str] = mapped_column(Text, nullable=True)
  law_info: Mapped[str] = mapped_column(String(length=64), nullable=True)
  user_id: Mapped[int] = mapped_column(Integer, nullable=False)
  created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
  updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<Clinics entity id = %r , title = %s>' % (self.id, self.title)


class ClinicPhoneModel(Base):
  __tablename__ = 'clinics_phones'
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(length=150), nullable=False)
  user_id: Mapped[int] = mapped_column(Integer, nullable=False)
  clinic_id: Mapped[int] = mapped_column(Integer, nullable=False)
  phone_number: Mapped[str] = mapped_column(String(length=64), nullable=True)
  is_main: Mapped[bool] = mapped_column(Boolean, nullable=True)
  created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
  updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<Clinic phone entity id = %r , title = %s>' % (self.id, self.title)