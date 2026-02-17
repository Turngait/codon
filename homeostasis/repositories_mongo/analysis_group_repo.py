# Just for example. Does not use anywhere

from app import db

class AnalysisGroupRepositories:
  def __init__(self, user_id: str):
    self._collection = 'analysis_groups'
    self._groups = []
    self._user_id = user_id

  async def get_group_for_user(self):
    await self._find_all_groups_for_user()
    return self._groups

  async def get_group_by_title_for_user(self, title):
    await self._find_group_by_title_for_user(title)
    return self._groups

  async def get_group_by_id_for_user(self, _id: str):
      return await db['analysis_groups'].find_one({"_id": _id, "user_id": self._user_id})

  async def _find_all_groups_for_user(self):
    cursor = db[self._collection].find({"user_id": self._user_id})
    async for group in cursor:
        group['_id'] = str(group['_id'])
        self._groups.append(group)

  async def _find_group_by_title_for_user(self, title):
      self._groups = await  db[self._collection].find_one({"user_id": self._user_id, "title": title})

  async def update_group_by_id(self, _id: str, data):
    await db[self._collection].update_one({"_id": _id}, {"$set": data})

  async def delete_group_by_id(self, _id:str):
    await db[self._collection].delete_one({"_id": _id, "user_id": self._user_id})

  async def insert_new_group(self, group):
    await db[self._collection].insert_one(group)
