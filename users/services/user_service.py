from datetime import datetime
from app import db

class User:
  async def createUser(self, user_info):
    old_user = await self.getUserByEmail(user_info.email)
    if old_user != None:
       return {'status': 4003, "msg": 'User already exist'}

    new_user = self.composeUser(user_info)
    try:
      await db.users_data.insert_one(new_user)
    except:
       return {'status': 5000, "msg": 'Server error'}
    return {'status': 200, "msg": 'User created'}


  async def getUserData(self, email):
    try:
      user_data = await self.getUserByEmail(email)
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
    user = await self.getUserByEmail(user_info.email)
    msg = 'User does not exist'
    status = 4003
    if user == None:
       return {'status': status, "msg": msg}
    
    try:
      user_data = user_info.model_dump()
      user["data"] = user_data["data"]
      await db.users_data.update_one({"_id": user["_id"]}, {"$set": user})
      status = 200
      msg = "Data was changed"
    except:
       status = 5000
       msg = 'Server error'
    return {'status': status, "msg": msg}


  def composeUser(self, user_info):
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


  async def getUserByEmail(self, email):
    return await db.users_data.find_one({"email": email})