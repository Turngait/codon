from datetime import datetime
from sqlalchemy import String, Text, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from typing import List

# from models.clinics_model import ClinicsModel
# from models.analysis_group_model import AnalysisGroupModel

class Base(DeclarativeBase):
  pass


#  TODO Move to another file
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
  

#  TODO Move to another file
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


class AnalysisModel(Base):
  __tablename__ = 'analysis'
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(length=150), nullable=False)
  description: Mapped[str] = mapped_column(Text, nullable=True)
  user_id: Mapped[int] = mapped_column(Integer, nullable=False)
  created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
  updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
  date: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
  group_id: Mapped[int] = mapped_column(Integer, ForeignKey('analysis_groups.id', ondelete='CASCADE'), nullable=False)
  group: Mapped["AnalysisGroupModel"] = relationship(foreign_keys=[group_id])
  doctors: Mapped[str] = mapped_column(Text, nullable=True)
  clinic_id: Mapped[int] = mapped_column(Integer, ForeignKey('clinics.id', ondelete='CASCADE'), nullable=False)
  clinic: Mapped["ClinicsModel"] = relationship(foreign_keys=[clinic_id])
  equipment: Mapped[str] = mapped_column(Text, nullable=True)


class ValuesModel(Base):
  __tablename__ = 'analysis_values'
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(length=64), nullable=False)
  volume: Mapped[str] = mapped_column(String(length=64), nullable=False)
  normal: Mapped[str] = mapped_column(String(length=64), nullable=False)
  description: Mapped[str] = mapped_column(Text, nullable=True)
  user_id: Mapped[int] = mapped_column(Integer, nullable=False)
  created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
  updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
  analysis_id: Mapped[int] = mapped_column(Integer, ForeignKey('analysis.id', ondelete='CASCADE'), nullable=False)
  analysis: Mapped["AnalysisModel"] = relationship(foreign_keys=[analysis_id])



  def __repr__(self):
    return '<Analyse entity id = %r, title = %s>' % (self.id, self.title)
