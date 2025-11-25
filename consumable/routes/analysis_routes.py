from typing import List
from pydantic import BaseModel
from fastapi_sqlalchemy import db
from sqlalchemy.orm import Session
from fastapi import Depends, Response

from app import app
from database import get_db
from services.analysis_service import Analysis
from services.analysis_groups_service import AnalysisGroupsService
from services.clinics_services import ClinicsServices
from models.test_model import Tests


class AddValueReq(BaseModel):
   analysis_id: int
   user_id: int
   title: str
   volume: str
   normal: str
   description: str

class AddValueWithAnalysisReq(BaseModel):
   title: str
   volume: str
   normal: str
   description: str

class AddValueWithIdReq(BaseModel):
  id: str
  title: str
  volume: str
  normal: str
  description: str

class AddAnalysisReq(BaseModel):
  user_id: int
  date: str
  title: str
  group_id: int
  doctors: str
  clinic_id: int
  equipment: str
  description: str
  values: List [AddValueWithAnalysisReq] = []

class GetAnalysisForUserReq(BaseModel):
   user_id: int

class DeleteAnalysisReq(BaseModel):
   analysis_id: int
   user_id: int

class DeleteValueReq(BaseModel):
   value_id: int
   user_id: int

class EditAnalysisReq(BaseModel):
  id: int
  user_id: int
  date: str
  title: str
  group_id: int
  doctors: str
  clinic_id: int
  equipment: str
  description: str

class EditValueReq(BaseModel):
   id: int
   user_id: int
   title: str
   volume: str
   normal: str
   description: str


@app.post("/analysis")
async def add_analysis(add_analysis_req: AddAnalysisReq, db: Session = Depends(get_db)):
    analysis = Analysis()
    return await analysis.add_analysis(add_analysis_req.model_dump(), db)

@app.post("/analysis/user")
async def get_analysis(req: GetAnalysisForUserReq, response: Response, db: Session = Depends(get_db)):
   analysis = Analysis()
   analysis_groups = AnalysisGroupsService()
   clinics = ClinicsServices()
   # TODO: delete user id from data
   groups_data = await analysis_groups.get_analysis_groups_for_user(req.user_id, db)
   analysis_data = await analysis.get_analysis_for_user_on_req(req.user_id, db)
   clinics_data = await clinics.get_clinics_for_user_on_req(req.user_id, db)

   status = 200 if clinics_data["status"] == 200 and analysis_data["status"] == 200 and groups_data["status"] == 200 else 500
   response.status_code = status

   return {"status": status, "data": {"analysis": analysis_data["data"], "groups": groups_data["data"], "clinics": clinics_data["data"]}}

@app.delete("/analysis")
async def delete_analysis(req: DeleteAnalysisReq, db: Session = Depends(get_db)):
   analysis = Analysis()
   return await analysis.delete_analysis(req.analysis_id, req.user_id, db)

@app.put("/analysis")
async def update_analysis(req: EditAnalysisReq, db: Session = Depends(get_db)):
   analysis = Analysis()
   return await analysis.edit_analysis(req.model_dump(), db)

@app.post("/analysis/value")
async def add_value_to_analysis(req: AddValueReq, db: Session = Depends(get_db)):
   analysis = Analysis()
   return await analysis.add_value(req.model_dump(), db)

@app.put("/analysis/value")
async def update_value_for_analysis(req: EditValueReq, db: Session = Depends(get_db)):
   analysis = Analysis()
   return await analysis.update_value(req.model_dump(), db)

@app.delete("/analysis/value")
async def delete_analysis_value(req: DeleteValueReq, db: Session = Depends(get_db)):
   analysis = Analysis()
   return await analysis.delete_analysis_value(req.value_id, req.user_id, db)


@app.post("/test")
async def test():
   tests = db.session.query(Tests).all()
   return {'status': 5000, "msg": 'Server error', "data": tests}