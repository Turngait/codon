from bson import ObjectId
from repositories.analysis_group_repo import AnalysisGroupRepositories


class AnalysisGroups:
  async def add_group(self, group):
    group_repo = AnalysisGroupRepositories(group["user_id"])

    old_group = await group_repo.get_group_by_title_for_user(group["title"])
    if old_group is None:
      new_group = self.compose_new_group(group)
      try:
        await group_repo.insert_new_group(new_group)
        return {'status': 200, "msg": 'Group was added'}
      except Exception as e:
        print(e)
        return {'status': 5000, "msg": 'Server error'}
    else:
      return {'status': 4003, "msg": 'Group already exist'}
  
  # Add exceptions
  async def get_analysis_groups_for_user(self, user_id: str):
    group_repo = AnalysisGroupRepositories(user_id)
    return await group_repo.get_group_for_user()
  
  async def delete_group(self, user_id: str, group_id: str):
    is_changed = 0
    group_repo = AnalysisGroupRepositories(user_id)
    try:
      group = await group_repo.get_group_by_id_for_user(ObjectId(group_id))
      if group is not None:
        await group_repo.delete_group_by_id(ObjectId(group_id))
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
    return {
      "title": data["title"],
      "description": data["description"],
      "user_id": data["user_id"],
    }