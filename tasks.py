
import requests
from celery import Celery
from pymongo import MongoClient
import time
import json

mongo_uri = "mongodb://mq:27017"
logs_table = "SC_Logs"
logs_database = "SC_Logs"
client =  MongoClient(mongo_uri);
db =  client[logs_database];
coll = db[logs_table]
app = Celery('tasks', broker='amqp://localhost//')

@app.task
def invokeURL(reqData):
    reqTime = time.time()

    # req as per action
    print(reqData)
    if(reqData['action'] == "get"):
        responseData = requests.get(reqData['url'],params = reqData['qs']).content
    else:
        responseData = requests.post(reqData['url'], data=json.dumps(reqData['post_json'])).content

    # Log the data
    coll.insert_one({"response": responseData,"resTime" : time.time(),"reqTime" : reqTime})


