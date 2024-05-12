from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

# 사용자 모델 정의
class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    events: Optional[List[Event]] = []

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "username": "junseok",
                "events": [],
            }
        }

# 사용자 로그인 모델 정의
class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example" : {
                "email" : "fastapi@packt.com",
                "password" : "strong!!!",
            }
        }