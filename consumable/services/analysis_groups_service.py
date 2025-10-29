from sqlalchemy.orm import Session
import datetime
from bson import ObjectId

from repositories.analysis_group_repo import AnalysisGroupRepositories
from models.analysis_group_model import AnalysisGroupModel


class AnalysisGroupsService:
  async def add_group(self, group, db: Session):
    new_group = self.compose_new_group(group)
    old_group = db.query(AnalysisGroupModel).filter(AnalysisGroupModel.title == new_group['title'] and AnalysisGroupModel.user_id == new_group['user_id']).first()
    if old_group is None:
      try:
        db_group = AnalysisGroupModel(
          title=new_group['title'], description=new_group['description'], user_id=new_group['user_id'], created_at=new_group['created_at'], updated_at=new_group['updated_at']
        )
        if not db_group:
          return {'status': 5000, "msg": 'Server error'}
        else:
          db.add(db_group)
          db.commit()
          db.refresh(db_group)
          return {'status': 200, "msg": 'Group was added', "data": {"group_id": db_group.id}}
      except Exception as e:
        print(e)
        return {'status': 5000, "msg": 'Server error'}
    else:
      return {'status': 4003, "msg": 'Group already exist'}
  
  # Add exceptions
  async def get_analysis_groups_for_user(self, user_id: str):
    group_repo = AnalysisGroupRepositories(user_id)
    return await group_repo.get_group_for_user()
  
  async def delete_group(self, user_id: str, group_id: str, db: Session):
    is_changed = 0
    
    old_group = db.query(AnalysisGroupModel).filter(AnalysisGroupModel.id == group_id and AnalysisGroupModel.user_id == user_id).first()
    try:
      if old_group is not None:
        db.delete(old_group)
        db.commit()
        is_changed = 1
    except Exception as e:
      print(e)
      return {'status': 5000, "msg": 'Server error'}

    if is_changed:
      return {'status': 200, "msg": 'Group was deleted'}
    else:
      return {'status': 4004, "msg": 'Group does not exist'}
  

  async def update_group(self, group):
    is_changed = 0
    group_repo = AnalysisGroupRepositories(group['user_id'])
    try:
      old_group = await group_repo.get_group_by_id_for_user(ObjectId(group['id']))
      if old_group is not None:
        del group['id']
        await group_repo.update_group_by_id(old_group["_id"], group)

        is_changed = 1
    except Exception as e:
      print(e)
      return {'status': 5000, "msg": 'Server error'}
    if is_changed:
      return {'status': 200, "msg": 'Group was updated'}
    else: return {'status': 4004, "msg": 'Group not found'}

  def compose_new_group(self, data):
    dt_now = datetime.datetime.now()
    formatted_dt = dt_now.strftime('%Y-%m-%d %H:%M:%S')
    return {
      "title": data["title"],
      "description": data["description"],
      "user_id": data["user_id"],
      "created_at": formatted_dt,
      "updated_at": formatted_dt
    }