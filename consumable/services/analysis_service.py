import datetime
from sqlalchemy.orm import Session # pyright: ignore[reportMissingImports]

from models.analysis_model import AnalysisModel, ValuesModel


class Analysis:
  async def add_analysis(self, data, db: Session):
    new_analyse = self._compose_new_analysis(data)
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
    
    
  async def get_analysis_for_user_on_req(self, user_id: str, db: Session):
    try:
      analysis = db.query(AnalysisModel).filter(AnalysisModel.user_id == user_id).all()
      values = db.query(ValuesModel).filter(ValuesModel.user_id == user_id).all()
      data = []
      for an in analysis:
         vals = [val for val in values if val.analysis_id == an.id]
         an.values = vals
         data.append(an)

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


  async def edit_analysis(self, analysis_data, db: Session):      
      try:
        analysis = self._get_analyse_by_user(analysis_data['id'], analysis_data['user_id'], db)
        if analysis is None:
            return {'status': 4004, "msg": 'Analysis not found'}
        
        analysis.title = analysis_data['title']
        analysis.date = analysis_data['date']
        analysis.group_id = analysis_data['group_id']
        analysis.doctors = analysis_data['doctors']
        analysis.clinic_id = analysis_data['clinic_id']
        analysis.description = analysis_data['description']

        db.commit()
      
        return {'status': 200, "msg": 'Analysis was updated'}
      except BaseException as err:
        print(err)
        return {'status': 5000, "msg": 'Server error'}


  async def add_value(self, data, db: Session):
      if len(data['values']) == 0:
         return {'status': 4001, "msg": 'There are 0 values in request'}
      analysis = self._get_analyse_by_user(data['analysis_id'], data['user_id'], db)
      new_values = []
      try:
        if analysis is None:
              return {'status': 4004, "msg": 'Analysis not found'}
        else:
          for val in data['values']:
            
            db_values = ValuesModel(
              title = val["title"],
              description = val["description"],
              volume = val["volume"],
              normal = val["normal"],
              user_id = data["user_id"],
              analysis_id = data["analysis_id"]
            )
            db.add(db_values)
            db.commit()
            db.refresh(db_values)
            new_values.append({
              "title": val["title"],
              "description": val["description"],
              "volume": val["volume"],
              "normal": val["normal"],
              "id": db_values.id
            })

          return {'status': 200, "msg": 'Values was added', "data": new_values}
      except BaseException as err:
        print(err)
        return {'status': 5000, "msg": 'Server error'}

  async def update_value(self, value_data, db: Session):
      try:
        value = self._get_value_by_user(value_data['id'], value_data['user_id'], db)
        if value is None:
            return {'status': 4004, "msg": 'Value not found'}
        
        value.title = value_data['title']
        value.volume = value_data['volume']
        value.normal = value_data['normal']
        value.description = value_data['description']

        db.commit()
      
        return {'status': 200, "msg": 'Value was updated'}
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
    return db.query(AnalysisModel).filter(AnalysisModel.id == analyse_id, AnalysisModel.user_id == user_id).first()
  
  def _get_value_by_user(self, id: int, user_id: int, db: Session):
    return db.query(ValuesModel).filter(ValuesModel.id == id, ValuesModel.user_id == user_id).first()
  
  def _compose_new_analysis(self, data):
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
  