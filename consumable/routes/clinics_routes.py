from sqlalchemy.orm import Session
from fastapi import Depends
from pydantic import BaseModel

from app import app
from database import get_db
from services.clinics_services import ClinicsServices



class AddClinicReq(BaseModel):
  title: str
  description: str
  law_info: str = ''
  main_site: str = ''
  user_id: int

class DeleteClinicReq(BaseModel):
   clinic_id: int
   user_id: int

class UpdateClinicReq(BaseModel):
  id: int
  title: str
  description: str
  law_info: str = ''
  main_site: str = ''
  user_id: int


@app.post("/clinic")
async def add_clinic(add_clinic_req: AddClinicReq, db: Session = Depends(get_db)):
    clinics_service = ClinicsServices()
    return await clinics_service.add_new_clinic(add_clinic_req.model_dump(), db)

@app.delete("/clinic")
async def delete_clinic(del_clinic_req: DeleteClinicReq, db: Session = Depends(get_db)):
    clinics_service = ClinicsServices()
    data = del_clinic_req.model_dump()
    return await clinics_service.delete_clinic(data['clinic_id'], data['user_id'], db)

@app.put('/clinic')
async def update_clinic(update_clinic_req: UpdateClinicReq, db: Session = Depends(get_db)):
   clinic_service = ClinicsServices()
   return await clinic_service.update_clinic(update_clinic_req.model_dump(), db)
   