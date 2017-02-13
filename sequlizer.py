from flask import Flask ,jsonify
from flask import request
import time
from datetime import datetime

app = Flask(__name__)

from tasks import invokeURL

@app.route("/set",methods=['POST','GET'])
def setTask():
	# print (request.args)
	# Getting params for task

	endpoint = request.args.get('endpoint', '')
	type = request.args.get('type', '')
	action = request.args.get('action', '')
	schedule = request.args.get('schedule', '')
	qs =  request.args.get('qs', '')
	post_json =  request.args.get('post_json', '')
	reqData = {"url": endpoint, "type": type, "qs": qs, "post_json": post_json,"action" : action}

	if(schedule == "now"):
		invokeURL.apply_async(([reqData]))

	else:
		timeNow = int(time.time())

		timeSchedule = int(int(schedule)/1000)
		timeInSec = timeSchedule - timeNow
			# datetime.strptime(schedule,"%Y-%m-%d %H:%M:%S")
		# timeSchedule = int((date -(datetime(1970,1,1))).total_seconds())
		# timeInSec = int((timeSchedule-timeNow))
		print("timeSchedule",timeSchedule)
		print("timeNow",timeNow)
		print("timeInSec",timeInSec)
		invokeURL.apply_async(([reqData]),countdown = timeInSec)

	list =	{"status" : "ok"}
	return jsonify(result= list)
