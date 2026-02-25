from sqlalchemy.orm import Session # pyright: ignore[reportMissingImports]
from fastapi import Depends # pyright: ignore[reportMissingImports]
from pydantic import BaseModel # pyright: ignore[reportMissingImports]

from app import app
from database import get_db
from services.clinics_services import ClinicsServices



class AddClinicReq(BaseModel):
  title: str
  description: str
  law_info: str = ''
  main_site: str = ''
  user_id: int
  phone: str = ''

class AddClinicPhoneReq(BaseModel):
  title: str
  user_id: int
  clinic_id: int
  phone_number: str
  is_main: bool

class AddClinicAddressReq(BaseModel):
   title: str
   user_id: int
   clinic_id: int
   address: str
   is_main: bool

class DeleteClinicReq(BaseModel):
   clinic_id: int
   user_id: int

class DeleteClinicPhoneReq(BaseModel):
   id: int
   user_id: int

class DeleteClinicAddressReq(BaseModel):
   id: int
   user_id: int

class UpdateClinicReq(BaseModel):
  id: int
  title: str
  description: str
  law_info: str = ''
  main_site: str = ''
  user_id: int

class UpdateClinicAddressReq(BaseModel):
  id: int
  title: str
  address: str = ''
  is_main: str = ''
  user_id: int

class UpdateClinicPhoneReq(BaseModel):
  id: int
  title: str
  phone_number: str = ''
  is_main: str = ''
  user_id: int


@app.post("/clinic")
async def add_clinic(add_clinic_req: AddClinicReq, db: Session = Depends(get_db)):
    clinics_service = ClinicsServices()
    return await clinics_service.add_new_clinic(add_clinic_req.model_dump(), db)

@app.put('/clinic')
async def update_clinic(update_clinic_req: UpdateClinicReq, db: Session = Depends(get_db)):
   clinic_service = ClinicsServices()
   return await clinic_service.update_clinic(update_clinic_req.model_dump(), db)

@app.delete("/clinic")
async def delete_clinic(del_clinic_req: DeleteClinicReq, db: Session = Depends(get_db)):
    clinics_service = ClinicsServices()
    data = del_clinic_req.model_dump()
    return await clinics_service.delete_clinic(data['clinic_id'], data['user_id'], db)

@app.post("/clinic/phone")
async def add_clinic_phone_api(add_clinic_phone_req: AddClinicPhoneReq, db: Session = Depends(get_db)):
    clinics_service = ClinicsServices()
    return await clinics_service.add_clinic_phone(add_clinic_phone_req.model_dump(), db)

@app.put("/clinic/phone")
async def update_clinic_phone(update_clinic_phone_req: UpdateClinicPhoneReq, db: Session = Depends(get_db)):
    clinics_service = ClinicsServices()
    return await clinics_service.update_clinic_phone(update_clinic_phone_req.model_dump(), db)

@app.delete("/clinic/phone")
async def delete_clinic_phone(del_clinic_phone_req: DeleteClinicPhoneReq, db: Session = Depends(get_db)):
    clinics_service = ClinicsServices()
    data = del_clinic_phone_req.model_dump()
    return await clinics_service.delete_clinic_phone(data['id'], data['user_id'], db)

@app.post("/clinic/address")
async def add_clinic_phone_api(add_clinic_address_req: AddClinicAddressReq, db: Session = Depends(get_db)):
    clinics_service = ClinicsServices()
    return await clinics_service.add_clinic_address(add_clinic_address_req.model_dump(), db)

@app.put("/clinic/address")
async def update_clinic_address(update_clinic_address_req: UpdateClinicAddressReq, db: Session = Depends(get_db)):
   clinics_service = ClinicsServices()
   return await clinics_service.update_clinic_address(update_clinic_address_req.model_dump(), db)

@app.delete("/clinic/address")
async def delete_clinic_address(del_clinic_phone_req: DeleteClinicAddressReq, db: Session = Depends(get_db)):
    clinics_service = ClinicsServices()
    data = del_clinic_phone_req.model_dump()
    return await clinics_service.delete_clinic_address(data['id'], data['user_id'], db)


   