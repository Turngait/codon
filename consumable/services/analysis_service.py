import datetime
from bson import ObjectId
from sqlalchemy.orm import Session

from repositories.analysis_repo import AnalysisRepositories
from models.analysis_model import AnalysisModel, ValuesModel


class Analysis:
  async def add_analysis(self, data, db: Session):
    new_analyse = self.compose_new_analysis(data)
    db_analyse = AnalysisModel(
       title=new_analyse["title"],
       description=new_analyse["description"],
       user_id=new_analyse["user_id"],
       created_at=new_analyse["created_at"],
       updated_at=new_analyse["updated_at"],
       date=new_analyse["date"],
       group_id=new_analyse["group_id"],
       doctors=new_analyse["doctors"],
       clinic_id=new_analyse["clinic_id"],
       equipment=new_analyse["equipment"]
    )

    
    try:
      db.add(db_analyse)
      db.commit()
      db.refresh(db_analyse)
      if len(data["values"]) >= 1:
        for val in data["values"]:
          db_values = ValuesModel(
            title = val["title"],
            description = val["description"],
            volume = val["volume"],
            normal = val["normal"],
            user_id = new_analyse["user_id"],
            analysis_id = db_analyse.id
          )
          db.add(db_values)
          db.commit()
          db.refresh(db_values)

      return {'status': 200, "msg": 'Analysis was added'}
    except Exception as e:
        print(e)
        return {'status': 5000, "msg": 'Server error'}
    
    
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
  

  async def delete_analysis(self, id: str, user_id: str, db: Session):
    try:
        analyse_for_del = self._get_analyse_by_user(id, user_id, db)

        if analyse_for_del == None:
           return {'status': 4004, "msg": 'Analyse not found'}
        else:
          db.delete(analyse_for_del)
          db.commit()

          return {'status': 200, "msg": 'Analyse was deleted'}
     
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


  async def add_value(self, data, db: Session):
      analysis = self._get_analyse_by_user(data['analysis_id'], data['user_id'], db)

      try:
        if analysis is None:
              return {'status': 4004, "msg": 'Analysis not found'}
        else:
          db_values = ValuesModel(
            title = data["title"],
            description = data["description"],
            volume = data["volume"],
            normal = data["normal"],
            user_id = data["user_id"],
            analysis_id = data["analysis_id"]
          )
          db.add(db_values)
          db.commit()
          db.refresh(db_values)
        return {'status': 200, "msg": 'Values was added'}
      except BaseException as err:
        print(err)
        return {'status': 5000, "msg": 'Server error'}

  async def update_value(self, data):
      analysis_repo = AnalysisRepositories(data["user_id"])
      is_find = 0
      try:
          analysis = await analysis_repo.get_analysis_for_user()
          if analysis is None:
              return {'status': 4004, "msg": 'Analysis not found'}

          for an in analysis['analysis']:
              if an["_id"] == data["analysis_id"]:
                  i = 0
                  for val in an["values"]:
                      if val["_id"] == data["value"]["id"]:
                          data["value"]["_id"] = data["value"]["id"]
                          del data["value"]["id"]
                          an["values"][i] = data["value"]
                          is_find += 1
                          break
                      i += 1

          if is_find:
              await analysis_repo.update_analysis_by_id(analysis["_id"], analysis)
              return {'status': 200, "msg": 'Value was updated'}
          else:
              return {'status': 4004, "msg": 'Analysis not found'}
      except BaseException as err:
        print(err)
        return {'status': 5000, "msg": 'Server error'}

  async def delete_analysis_value(self, id: int, user_id: int, db: Session):
     try:
        value_for_del = self._get_value_by_user(id, user_id, db)

        if value_for_del == None:
           return {'status': 4004, "msg": 'Value not found'}
        else:
          db.delete(value_for_del)
          db.commit()

          return {'status': 200, "msg": 'Value was deleted'}
     
     except BaseException as err:
        print(err)
        return {'status': 5000, "msg": 'Server error'}

  def _get_analyse_by_user(self, analyse_id: int, user_id: int, db: Session):
    return db.query(AnalysisModel).filter(AnalysisModel.id == analyse_id and AnalysisModel.user_id == user_id).first()
  
  def _get_value_by_user(self, id: int, user_id: int, db: Session):
    return db.query(ValuesModel).filter(ValuesModel.id == id and ValuesModel.user_id == user_id).first()
  
  def compose_new_analysis(self, data):
    dt_now = datetime.datetime.now()
    formatted_dt = dt_now.strftime('%Y-%m-%d %H:%M:%S')

    return {
      "user_id": data['user_id'],
      "date": data["date"],
      "title": data["title"],
      "group_id": data['group_id'],
      "doctors": data['doctors'],
      "clinic_id": data['clinic_id'],
      "description": data['description'],
      "equipment": data['equipment'],
      "created_at": formatted_dt,
      "updated_at": formatted_dt
    }
  