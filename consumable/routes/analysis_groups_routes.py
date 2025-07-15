from pydantic import BaseModel
from app import app
from services.analysis_groups_service import AnalysisGroups

class AnalysisGroup(BaseModel):
  title: str
  description: str
  user_id: str

class DeleteAnalysisGroup(BaseModel):
   group_id: str
   user_id: str

class UpdateGroup(BaseModel):
  id: str
  title: str
  description: str
  user_id: str


@app.post("/analysis_groups")
async def add_analysis_group(analysis_group_req: AnalysisGroup):
    analysis_groups = AnalysisGroups()
    return await analysis_groups.add_group(analysis_group_req.model_dump())


@app.delete("/analysis_groups")
async def delete_analysis_group(del_group_req: DeleteAnalysisGroup):
    analysis_groups = AnalysisGroups()
    data = del_group_req.model_dump()
    return await analysis_groups.delete_group(data['user_id'], data['group_id'])


@app.put("/analysis_groups")
async def update_analysis_group(update_group_dto: UpdateGroup):
    analysis_groups = AnalysisGroups()
    return await analysis_groups.update_group(update_group_dto.model_dump())