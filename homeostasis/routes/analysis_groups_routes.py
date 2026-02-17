from sqlalchemy.orm import Session
from fastapi import Depends
from pydantic import BaseModel

from app import app
from database import get_db
from services.analysis_groups_service import AnalysisGroupsService


class AddAnalysisGroupReq(BaseModel):
  title: str
  description: str
  user_id: int

class DeleteAnalysisGroupReq(BaseModel):
   group_id: int
   user_id: int

class UpdateGroupReq(BaseModel):
  id: int
  title: str
  description: str
  user_id: int


@app.post("/analysis_groups")
async def add_analysis_group(add_analysis_group_req: AddAnalysisGroupReq, db: Session = Depends(get_db)):
    analysis_groups = AnalysisGroupsService()
    return await analysis_groups.add_group(add_analysis_group_req.model_dump(), db)


@app.delete("/analysis_groups")
async def delete_analysis_group(del_group_req: DeleteAnalysisGroupReq, db: Session = Depends(get_db)):
    analysis_groups = AnalysisGroupsService()
    data = del_group_req.model_dump()
    return await analysis_groups.delete_group(data['user_id'], data['group_id'], db)


@app.put("/analysis_groups")
async def update_analysis_group(update_group_req: UpdateGroupReq, db: Session = Depends(get_db)):
    analysis_groups = AnalysisGroupsService()
    return await analysis_groups.update_group(update_group_req.model_dump(), db)