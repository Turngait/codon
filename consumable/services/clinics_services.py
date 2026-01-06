from sqlalchemy.orm import Session # pyright: ignore[reportMissingImports]
import datetime

from models.clinics_model import ClinicsModel, ClinicPhoneModel


class ClinicsServices:
  async def add_new_clinic(self, clinic, db: Session):
    new_clinic = self._compose_new_clinic(clinic)
    old_clinic = db.query(ClinicsModel).filter(ClinicsModel.title == clinic['title'], ClinicsModel.user_id == clinic['user_id']).first()
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
          if len(new_clinic['phone']) > 0:
            await self.add_clinic_phone({'title': 'Main phone', 'user_id': new_clinic['user_id'], 'clinic_id': db_clinic.id, 'phone_number': new_clinic['phone'], 'is_main': True}, db)
          return {'status': 200, "msg": 'Clinic was added', "data": {"clinic_id": db_clinic.id}}
      except Exception as e:
        print(e)
        return {'status': 5000, "msg": 'Server error'}
      
    else:
      return {'status': 4003, "msg": 'Clinic already exist'}
  
  async def get_clinics_for_user_on_req(self, user_id: str, db: Session):
    try:
      clinics = db.query(ClinicsModel).filter(ClinicsModel.user_id == user_id).all()

      return {'status': 200, "msg": 'Clinics', "data": clinics}
    except Exception as e:
        print(e)
        return {'status': 5000, "msg": 'Server error'}
    

  async def delete_clinic(self, clinic_id, user_id, db: Session):
    is_changed = 0

    try:
      old_clinic = db.query(ClinicsModel).filter(ClinicsModel.id == clinic_id, ClinicsModel.user_id == user_id).first()
    
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
  
  async def update_clinic(self, new_clinic_data, db: Session):
    try:
      clinic_for_update = db.query(ClinicsModel).filter(ClinicsModel.id == new_clinic_data['id'], ClinicsModel.user_id == new_clinic_data['user_id']).first()
      if clinic_for_update:
        clinic_for_update.title = new_clinic_data['title']
        clinic_for_update.description = new_clinic_data['description']
        clinic_for_update.law_info = new_clinic_data['law_info']
        clinic_for_update.main_site = new_clinic_data['main_site']

        db.commit()

        return {'status': 200, "msg": 'Clinic was updated'}
      else:
        return {'status': 4004, "msg": 'Clinic does not exist'}
    except Exception as e:
      print(e)
      return {'status': 5000, "msg": 'Server error'}

  async def add_clinic_phone(self, clinic_phone_data, db: Session):    
    try:
      if clinic_phone_data['is_main'] and clinic_phone_data['clinic_id']:
        is_main_exist = db.query(ClinicPhoneModel).filter(ClinicPhoneModel.is_main == 1, ClinicPhoneModel.user_id == clinic_phone_data['user_id'], ClinicPhoneModel.clinic_id == clinic_phone_data['clinic_id']).first()
        if is_main_exist is not None:
          return {'status': 4003, "msg": 'Main clinic phone is exist'}

      db_clinic_phone = ClinicPhoneModel (
        title = clinic_phone_data['title'],
        user_id = clinic_phone_data['user_id'],
        clinic_id = clinic_phone_data['clinic_id'],
        phone_number = clinic_phone_data['phone_number'],
        is_main = clinic_phone_data['is_main']
      )

      db.add(db_clinic_phone)
      db.commit()
      db.refresh(db_clinic_phone)
      return {'status': 200, "msg": 'Clinic phone was added', "data": {"phone_id": db_clinic_phone.id}}
    except Exception as e:
      print(e)
      return {'status': 5000, "msg": 'Server error'}
  
  def _compose_new_clinic(self, data):
    dt_now = datetime.datetime.now()
    formatted_dt = dt_now.strftime('%Y-%m-%d %H:%M:%S')

    return {
      "title": data["title"],
      "description": data["description"],
      "main_site": data["main_site"],
      "law_info": data["law_info"],
      "user_id": data["user_id"],
      "phone": data["phone"],
      "created_at": formatted_dt,
      "updated_at": formatted_dt
    }
