"""
    DAO AUTH MODULES
"""
import traceback
from fastapi.exceptions import HTTPException
from fastapi import status
from config import mongo
import random


def get_data():
    try:
        client, collumn = mongo.account()
        data = collumn.find()
        result = []
        for detail in data:
            print(detail)
            result.append(detail)
        client.close()
        return result
    except:
        traceback.print_exc()
        raise HTTPException(status.HTTP_502_BAD_GATEWAY, "Failed get data")


def post_data(data:dict):
    try:
        client, collumn = mongo.account()
        datas = data
        datas['_id'] = random.randint(000000,999999)
        collumn.insert_one(datas)
        client.close()
        return "Data Has Been Inserted"
    except:
        traceback.print_exc()
        raise HTTPException(status.HTTP_502_BAD_GATEWAY, "Failed Post Data")

def put_data(username:str, new_name:str):
    try:
        client, collumn = mongo.account()
        checking = collumn.find_one({'username':username})
        if checking is not None:
            query_find = {"username":username}
            new_value = {'$set':{"username":new_name}}
            updated = collumn.update_one(query_find, new_value)
            return "Update "+name+" successfully"
    except:
        traceback.print_exc()
        raise HTTPException(status.HTTP_502_BAD_GATEWAY, "Failed Update Data")


def delete_data(username:str):
    try:
        client, collumn = mongo.account()
        checking = collumn.find_one({'username':username})
        if checking is not None:
            collumn.delete_one({'username':username})
            return "Delete "+name+" has been successfully"
        else:
            raise HTTPException(status.HTTP_417_EXPECTATION_FAILED, "Data Not Found")
    except:
        traceback.print_exc()
        raise HTTPException(status.HTTP_502_BAD_GATEWAY, "Failed Delete Data")
