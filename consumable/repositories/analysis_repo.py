from app import db

class AnalysisRepositories:
  def __init__(self, user_id: str):
    self._collection = 'analysis'
    self._analysis = []
    self._user_id = user_id

  async def get_analysis_for_user(self):
    await self._find_all_analysis_for_user()
    return self._analysis

  async def _find_all_analysis_for_user(self):
    self._analysis = await db[self._collection].find_one({"user_id": self._user_id})

  async def update_analysis_by_id(self, _id: str, data):
    await db[self._collection].update_one({"_id": _id}, {"$set": data})

  async def insert_new_analysis(self, analysis):
    await db[self._collection].insert_one(analysis)
