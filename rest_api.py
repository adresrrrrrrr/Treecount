from flask import Flask,request,Response
#from flask_pymongo import PyMongo
from mongosave import mongosave
import time

import pdb
app= Flask(__name__)


@app.route('/savedata',methods=["GET","POST"])
def index():
	#pdb.set_trace()
	imgdata=request.form['image']
	filename ="audience.jpg" 
	timestmp = int(time.time())
	filename= str(timestmp)+"_"+filename
	opfile="uploads/"+filename
	with open(opfile,"wb") as imgFile:
		imgFile.write(imgdata.decode('base64'))
	mongoDB=mongosave('wproject')
	save_resp=mongoDB.save_mongodb(path=opfile,image_name=filename,table_name="Treedata")
	search_resp=mongoDB.search(table_name="Treedata")
	#pdb.set_trace()

app.run(host='0.0.0.0',port=5000)
#pdb.set_trace()	
