"""
    ELASTIC ROUTE MODULE
"""
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from config import elastic
app = APIRouter()

@app.get("/")
def get_data():
    try:
        es = elastic.connect()
    except:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Failed get data")

@app.post("/")
def post_data():
    try:
        es = elastic.connect()
        es.index()
    except expression as identifier:
        pass
