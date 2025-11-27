from sqlalchemy.orm import Session # pyright: ignore[reportMissingImports]

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
        return {'status': 200, "msg": 'User data', "data": user_data}
      else:
        return {'status': 4003, "msg": 'User does not exist'}
    except Exception as e:
       return {'status': 5000, "msg": 'Server error'}


  async def updateUserData(self, user_info, db):
    try:
      user = await self.self.__getUserByID(user_info['user_id'], db)

      if user is None:
        return {'status': 4003, "msg": 'User does not exist'}
      
      user.biological_gender = user_info['biological_gender']
      user.data_birth = user_info['data_birth']
      user.weight = user_info['weight']
      user.height = user_info['height']

      db.commit()
    
    except Exception as e:
      return {'status': 5000, "msg": 'Server error'}

  async def __getUserByID(self, user_id, db: Session):
    return db.query(UsersDataModel).filter(UsersDataModel.user_id == user_id).first()