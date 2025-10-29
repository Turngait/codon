from sqlalchemy.orm import Session
import datetime

from models.clinics_model import ClinicsModel


class ClinicsServices:
  async def add_new_clinic(self, clinic, db: Session):
    print(clinic)
    new_clinic = self.compose_new_clinic(clinic)
    old_clinic = db.query(ClinicsModel).filter(ClinicsModel.title == clinic['title'] and ClinicsModel.user_id == clinic['user_id']).first()
    if old_clinic == None:
      try:
        db_clinic = ClinicsModel(
          title=new_clinic['title'],
          description=new_clinic['description'],
          law_info= new_clinic['law_info'],
          main_site= new_clinic['main_site'],
          user_id=new_clinic['user_id'],
          created_at=new_clinic['created_at'],
          updated_at=new_clinic['updated_at']
        )
        if not db_clinic:
          return {'status': 5000, "msg": 'Server error'}
        else:
          db.add(db_clinic)
          db.commit()
          db.refresh(db_clinic)
          print(db_clinic)
          return {'status': 200, "msg": 'Clinic was added', "data": {"group_id": db_clinic.id}}
      except Exception as e:
        print(e)
        return {'status': 5000, "msg": 'Server error'}
      
    else:
      return {'status': 4003, "msg": 'Clinic already exist'}
    

  async def delete_clinic(self, clinic_id, user_id, db: Session):
    is_changed = 0
    
    old_clinic = db.query(ClinicsModel).filter(ClinicsModel.id == clinic_id and ClinicsModel.user_id == user_id).first()
    try:
      if old_clinic is not None:
        db.delete(old_clinic)
        db.commit()
        is_changed = 1
    except Exception as e:
      print(e)
      return {'status': 5000, "msg": 'Server error'}

    if is_changed:
      return {'status': 200, "msg": 'Clinic was deleted'}
    else:
      return {'status': 4004, "msg": 'Clinic does not exist'}
  
  def compose_new_clinic(self, data):
    dt_now = datetime.datetime.now()
    formatted_dt = dt_now.strftime('%Y-%m-%d %H:%M:%S')

    return {
      "title": data["title"],
      "description": data["description"],
      "main_site": data["main_site"],
      "law_info": data["law_info"],
      "user_id": data["user_id"],
      "created_at": formatted_dt,
      "updated_at": formatted_dt
    }