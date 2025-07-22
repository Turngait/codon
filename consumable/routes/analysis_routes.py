from pydantic import BaseModel
from typing import List
from app import app
from services.analysis_service import Analysis
from services.analysis_groups_service import AnalysisGroups

class AnalysisData(BaseModel):
  title: str
  volume: str
  normal: str
  description: str

class AnalysisDataWithId(BaseModel):
  id: str
  title: str
  volume: str
  normal: str
  description: str

class AddAnalysis(BaseModel):
  user_id: str
  date: str
  title: str
  values: List[AnalysisData]
  group_id: str
  doctors: List[str]
  clinic: str
  equipment: str
  description: str

class GetAnalysis(BaseModel):
   user_id: str

class DeleteAnalysis(BaseModel):
   analysis_id: str
   user_id: str

class EditAnalysis(BaseModel):
  user_id: str
  date: str
  title: str
  values: List[AnalysisData]
  group_id: str
  doctors: List[str]
  clinic: str
  equipment: str
  description: str

class AddValueReq(BaseModel):
    user_id: str
    analysis_id: str
    value: AnalysisData

class EditValueReq(BaseModel):
    user_id: str
    analysis_id: str
    value: AnalysisDataWithId


@app.post("/analysis")
async def add_user_info(add_analysis_req: AddAnalysis):
    analysis = Analysis()
    return await analysis.add_analysis(add_analysis_req.model_dump())

@app.post("/analysis/user")
async def get_analysis(req: GetAnalysis):
   analysis = Analysis()
   analysis_groups = AnalysisGroups()
   groups = await analysis_groups.get_analysis_groups_for_user(req.user_id)
   return await analysis.get_analysis_for_user_on_req(req.user_id, groups)

@app.delete("/analysis")
async def delete_analysis(req: DeleteAnalysis):
   analysis = Analysis()
   return await analysis.delete_analysis(req.analysis_id, req.user_id)

@app.put("/analysis")
async def update_analysis(req: EditAnalysis):
   analysis = Analysis()
   return await analysis.edit_analysis(req.model_dump())

@app.post("/analysis/value")
async def add_value_to_analysis(req: AddValueReq):
   analysis = Analysis()
   return await analysis.add_value(req.model_dump())

@app.put("/analysis/value")
async def update_value_to_analysis(req: EditValueReq):
   analysis = Analysis()
   return await analysis.update_value(req.model_dump())