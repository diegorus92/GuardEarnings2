from pymongo import MongoClient
from Data.models import Guard

client = MongoClient("localhost", 27017)
db = client.guard_earnings2


def getGuards():
    return db.guard.find()
def getWorksByGuard(guard_name, guard_lastname):
    return db.guard.find_one({"$and": [{"name": guard_name}, {"last_name": guard_lastname}]})
def getWorks(guardId):
    return db.works.find({"guard_id": guardId})

def insertWork(object):
    return db.works.insert_one(object)

def insertManyWorks(list):
    return db.works.insert_many(list)

def insertGuard(name, last_name, date_of_birth):
    return db.guard.insert_one({"name": name, "last_name": last_name, "date_of_birth": date_of_birth})

def deleteGuard(guardId):
    return db.guard.delete_one({"_id": guardId})
