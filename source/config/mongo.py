"""
    MONGO CONFIG MODULE
"""
import pymongo
from fastapi.exceptions import HTTPException
from fastapi import status

def account():
    try:
        client = pymongo.MongoClient("mongodb://admin:jaringan123@192.168.29.86:27017/")
        database = client['management']
        coll = database['accounts']
        return client, coll
    except:
        raise HTTPException(status.HTTP_502_BAD_GATEWAY,"Failed Connect Database")
