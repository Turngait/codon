from datetime import datetime
from sqlalchemy.orm import Session

from models.users_data_model import UsersDataModel


class User:
  async def createUser(self, user_info, db: Session):
    old_user = await self.__getUserByID(user_info["user_id"], db)
    if old_user != None:
       return {'status': 4003, "msg": 'User already exist'}
    
    db_user_data = UsersDataModel(
      status=1,
      user_timezone="",
      user_id=user_info["user_id"],
      isBanned=False,
      biological_gender=user_info["data"]["sex"],
      data_birth=user_info["data"]["data_birth"],
      weight=user_info["data"]["weight"],
      height=user_info["data"]["height"],
      lang_interface=user_info["settings"]["lang"],
      theme_interface=user_info["settings"]["theme"]
    )

    try:
      db.add(db_user_data)
      db.commit()
      db.refresh(db_user_data)
      return {'status': 200, "msg": 'User created'}
    except Exception as e:
       print(e)
       return {'status': 5000, "msg": 'Server error'}


  async def getUserData(self, user_id, db: Session):
    try:
      user_data = await self.__getUserByID(user_id, db)
      if user_data:
        data = {
          "user_id": str(user_data["_id"]),
          "data": user_data['data'],
          "settings": user_data['settings'],
          "onboarding": user_data['onboarding'],
        }
        return {'status': 200, "msg": 'User data', "data": data}
      else:
        return {'status': 4003, "msg": 'User does not exist'}
    except:
       return {'status': 5000, "msg": 'Server error'}


  async def updateUserData(self, user_info):
    # user = await self.self.__getUserByID(email, db)
    # msg = 'User does not exist'
    # status = 4003
    # if user == None:
    #    return {'status': status, "msg": msg}
    
    # try:
    #   user_data = user_info.model_dump()
    #   user["data"] = user_data["data"]
    #   await db.users_data.update_one({"_id": user["_id"]}, {"$set": user})
    #   status = 200
    #   msg = "Data was changed"
    # except:
    #    status = 5000
    #    msg = 'Server error'
    return {'status': "status", "msg": "msg"}


  def __composeUser(self, user_info):
    return {
        "email": user_info.email,
        "status": "user",
        "isBanned": False,
        "data": {
          "sex": user_info.data.sex,
          "age": user_info.data.age,
          "weight": user_info.data.weight,
          "height": user_info.data.height,
        },
      "settings": {
        "lang": user_info.settings.lang,
        "theme": user_info.settings.theme,
      },
      "onboarding": {
        "firstTime": False
      },
      "createdAt": datetime.today().strftime('%Y-%m-%d')
    }


  async def __getUserByID(self, user_id, db: Session):
    return db.query(UsersDataModel).filter(UsersDataModel.user_id == user_id).first()