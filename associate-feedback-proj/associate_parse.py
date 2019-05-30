import pymongo
from pymongo import MongoClient 
import json


filename = "associate-data"

descs = {}
lineno = 0

client = MongoClient('localhost', 27017)

db = client.flights

collection = db['associateFeedback']


with open(filename) as fn:
    for line in fn:
        description = line.strip()
        lineno = lineno + 1
        #print("description - ",description)
        descs["comment"] = description
        descs["_id"] = lineno
        collection.insert_one(descs)
        

