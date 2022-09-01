""" AUTH ROUTE MODULES """

from fastapi import APIRouter
from typing import List 
from model import mongo
from scheme import mongo as models
app = APIRouter()

@app.get("/get")
def get_data():
    return mongo.get_data()

@app.post("/post")
def post_data(model:List[models.PostData]):
    return mongo.post_data(model.dict())

@app.put("/put")
def put_data(name:str, new_name:str):
    return mongo.put_data(name, new_name)

@app.delete("/delete")
def detele_data(name:str):
    return mongo.delete_data(name)
