from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends

from app import app
from services.user_service import User
from database import get_db


class UserData(BaseModel):
  sex: str
  data_birth: str
  weight: float
  height: float

class UserSettings(BaseModel):
  lang: str
  theme: str

class UserInfoReq(BaseModel):
  user_id: int
  data: UserData
  settings: UserSettings

class UserGetInfo(BaseModel):
  user_id: int

class UpdateUserData(BaseModel):
  email: str
  data: UserData


@app.post("/user")
async def addUserInfo(user_info_req: UserInfoReq, db: Session = Depends(get_db)):
    user = User()
    return await user.createUser(user_info_req.model_dump(), db)

@app.post("/getdata")
async def getUserInfo(user_info: UserGetInfo, db: Session = Depends(get_db)):
    user = User()
    return await user.getUserData(user_info.email, db);

@app.put("/updatedata")
async def updateUserInfo(user_info: UpdateUserData):
    user = User()
    return await user.updateUserData(user_info);