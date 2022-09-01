"""
    ELASTIC MODEL
"""
from pydantic import BaseModel, EmailStr

class ElasticData(BaseModel):
    username:str
    name:str
    email:EmailStr
    phone:str
    password:str

