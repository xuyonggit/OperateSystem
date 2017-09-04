# -*- coding: utf-8 -*-
import pymongo
from bson.objectid import ObjectId


def Conn():
    return pymongo.MongoClient('192.168.130.183', 27017)


def mongo_query(List):
    C = Conn()
    db = C.ywxt.Version
    if List['i_type'] == "":
        dic = {"version": int(List['i_version'])}
    else:
        dic = {"version": int(List['i_version']), "type": int(List['i_type'])}
    return db.find_one(dic)