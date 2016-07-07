from flask import Flask,request,Response,jsonify
#from flask_pymongo import PyMongo
from mongosave import mongosave
import time
import json
import pdb
app= Flask(__name__,static_url_path='/home/ubuntu/wireless_REST/static/')


@app.route('/savedata',methods=["GET","POST"])
def index():
	imgdata=request.form['photostring']
	filename =request.form["photoname"]
	filename=filename+".jpg"
	latt = request.form["lat"]
	longt = request.form["long"]
	treename=request.form["treename"]
	ownername=request.form["owner"]
	timestmp = time.ctime()
	filename= filename
	opfile="uploads/"+filename
	with open(opfile,"wb") as imgFile:
		imgFile.write(imgdata.decode('base64'))
	mongoDB=mongosave('wproject')
	save_resp=mongoDB.save_mongodb(path=opfile,image_name=filename,latitude=latt,longitude=longt,timestamp=timestmp,table_name="Treedata",treename=treename,owner=ownername)
	search_resp=mongoDB.search(table_name="Treedata")
	return "Successfully saved"

@app.route('/getcoords',methods=["GET","POST"])
def getcoord():
	mongoDB=mongosave('wproject')
	records=mongoDB.retrieveAll(table_name="Treedata")
	respData=[]
	for record in records:
		record.pop("_id",None)
		respData.append(record)
	return json.dumps(respData)

@app.route('/displaymap',methods=["GET"])
def static_page():
	return app.send_static_file('test.html')

@app.route('/<path:path>',methods=["GET"])
def static_sheet(path):
	return app.send_static_file(path)


#pdb.set_trace()	
app.run(host='0.0.0.0',port=5000)
