from app import db
from datetime import datetime

class Analysis(db.Model):
  __tablename__ = 'analysis'
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(length=150), nullable=False)
  description = db.Column(db.Text, nullable=True)
  user_id = db.Column(db.Integer, nullable=False)
  date = db.Column(db.DateTime, default=datetime.utcnow)
  group_id = db.Column(db.Integer, db.ForeignKey('clinics.id'), nullable=False)
  doctors = db.Column(db.Text, nullable=True)
  clinic_id = db.Column(db.Integer, db.ForeignKey('clinics.id'), nullable=False)
  equipment = db.Column(db.Text, nullable=True)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<Analyse %r>' % self.id
