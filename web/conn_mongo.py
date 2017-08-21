# -*- coding: utf-8 -*-
import pymongo


def Conn():
    return pymongo.MongoClient('192.168.130.183', 27017)


def mongo_query(List):
    version = List['i_version']
    type = List['i_type']
    C = Conn()
    db = C.ywxt
    out_data = []
    return db.Version.find_one()