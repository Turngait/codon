from datetime import datetime
from bson import ObjectId
from repositories.analysis_repo import AnalysisRepositories


class Analysis:
  async def add_analysis(self, data):
    analysis_repo = AnalysisRepositories(data["user_id"])
    old_analysis = await analysis_repo.get_analysis_for_user()
    
    if old_analysis is None:
      new_analysis = self.compose_new_analysis(data)
      try:
        await analysis_repo.insert_new_analysis(new_analysis)
      except Exception as e:
        print(e)
        return {'status': 5000, "msg": 'Server error'}
    else:
      print(old_analysis)
      old_analysis['analysis'].append(self.compose_for_existing_analysis(data))
      await analysis_repo.update_analysis_by_id(old_analysis["_id"], old_analysis)

    return {'status': 200, "msg": 'Analysis was added'}
    
    
  async def get_analysis_for_user_on_req(self, user_id: str, groups):
    data = {}
    analysis_repo = AnalysisRepositories(user_id)

    try:
      analysis = await analysis_repo.get_analysis_for_user()
      if analysis is not None:
          data['analysis'] = analysis['analysis']
          data['groups'] = groups
      return {'status': 200, "msg": 'Analysis', "data": data}
    except Exception as e:
        print(e)
        return {'status': 5000, "msg": 'Server error'}
  

  async def delete_analysis(self, _id: str, user_id: str):
    is_changed = 0
    analysis_repo = AnalysisRepositories(user_id)
    try:
        analysis = await analysis_repo.get_analysis_for_user()
        if analysis is None:
           return {'status': 4004, "msg": 'Analysis not found'}
        for i, analyse in enumerate(analysis["analysis"], start=0):
          
          if str(analyse["_id"]) == _id:
             analysis["analysis"].remove(analyse)
             is_changed = 1
             break
          if analyse["values"] is not None and len(analyse["values"]):
             for v, value in enumerate(analyse["values"], start=0):
              if str(value["_id"]) == _id:
                 analyse["values"].remove(value)
                 is_changed = 1
                 break
        if is_changed == 1:
          print(analysis["_id"])
          await analysis_repo.update_analysis_by_id(analysis["_id"], analysis)
          return {'status': 200, "msg": 'Analyse was deleted'}
        else:
           return {'status': 4004, "msg": 'Analysis not found'}
    except BaseException as err:
      print(err)
      return {'status': 5000, "msg": 'Server error'}


  async def edit_analysis(self, analysis):
    analysis_repo = AnalysisRepositories(analysis["user_id"])
    try:
      old_analysis = await analysis_repo.get_analysis_for_user()
      if old_analysis is None:
        return {'status': 4004, "msg": 'Analysis not found'}
      del analysis["user_id"]
      old_analysis["analysis"] = analysis
      await analysis_repo.update_analysis_by_id(old_analysis["_id"], old_analysis)

      return {'status': 200, "msg": 'Analyse was updated'}
    
    except BaseException as err:
      print(err)
      return {'status': 5000, "msg": 'Server error'}


  def compose_new_analysis(self, data):
    for val in data['values']:
      val["_id"] = str(ObjectId())

    return {
      "user_id": data['user_id'],
      "analysis": [{
        "_id": str(ObjectId()),
        "date": data["date"],
        "title": data["title"],
        "values": data['values'],
        "group_id": data['group_id'],
        "doctors": data['doctors'],
        "clinic": data['clinic'],
        "description": data['description'],
        "equipment": data['equipment'],
        }],
      "createdAt": datetime.today().strftime('%Y-%m-%d')
    }
  

  def compose_for_existing_analysis(self, data):
      for val in data['values']:
        val["_id"] = str(ObjectId())
      return {
        "_id": str(ObjectId()),
        "date": data["date"],
        "title": data["title"],
        "values": data['values'],
        "group_id": data['group_id'],
        "doctors": data['doctors'],
        "clinic": data['clinic'],
        "description": data['description'],
        "equipment": data['equipment'],
    }
