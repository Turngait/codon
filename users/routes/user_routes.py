from pydantic import BaseModel
from app import app, db
from services.user_service import User

class UserData(BaseModel):
  sex: str
  age: int
  weight: float
  height: float

class UserSettings(BaseModel):
  lang: str
  theme: str

class UserInfo(BaseModel):
  email: str
  data: UserData
  settings: UserSettings

class UserGetInfo(BaseModel):
  email: str

class UpdateUserData(BaseModel):
  email: str
  data: UserData


@app.post("/user")
async def addUserInfo(user_info: UserInfo):
    user = User()
    return await user.createUser(user_info)

@app.post("/getdata")
async def addUserInfo(user_info: UserGetInfo):
    user = User()
    return await user.getUserData(user_info.email);

@app.put("/updatedata")
async def updateUserInfo(user_info: UpdateUserData):
    user = User()
    return await user.updateUserData(user_info);