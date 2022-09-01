"""
AUTH SCHEMAS
"""
from pydantic import BaseModel, EmailStr, Field, validator
from config import mongo
import hashlib

class PostData(BaseModel):
    username:str = Field(..., example="johndoe")
    fullname:str = Field(..., example="John Doe")
    email:EmailStr = Field(...,example="name@mail.com" )
    phone:str = Field(..., example="+62888991112222")
    password:str = Field(..., example="JohnDoe123")

    @validator('username')
    def check_username(cls, value):
        try:
            client, coll = mongo.account()
            checker = coll.find_one({'username':value})
            print(checker)
            if checker is None:
                return value
            else:
                return ValueError("username already used!")
        except:
            return ValueError("Failed connect database")

    @validator('password')
    def hashing_password(cls, value):
        return hashlib.sha256(value.encode()).hexdigest() 
