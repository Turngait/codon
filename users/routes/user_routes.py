from pydantic import BaseModel # pyright: ignore[reportMissingImports]
from sqlalchemy.orm import Session # pyright: ignore[reportMissingImports]
from fastapi import Depends # pyright: ignore[reportMissingImports]

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
  user_id: int
  biological_gender: str
  data_birth: str
  weight: str
  height: str


@app.post("/user")
async def addUserInfo(user_info_req: UserInfoReq, db: Session = Depends(get_db)):
    user = User()
    return await user.createUser(user_info_req.model_dump(), db)

@app.post("/getdata")
async def getUserInfo(user_info: UserGetInfo, db: Session = Depends(get_db)):
    user = User()
    return await user.getUserData(user_info.user_id, db);

@app.put("/updateuserdata")
async def updateUserInfo(user_info: UpdateUserData, db: Session = Depends(get_db)):
    user = User()
    return await user.updateUserData(user_info.model_dump(), db);
