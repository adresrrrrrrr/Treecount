import pymongo
from pymongo import MongoClient
import pdb
class mongosave:
	def __init__(self,dbname):
		mclient=MongoClient()
		self.mDB=mclient[dbname]
	
	def save_mongodb(self,**kwargs):
		try:
			mDBTable=self.mDB[kwargs["table_name"]]
			lat=kwargs["latitude"]
			longt=kwargs["longitude"]
			pdb.set_trace()	
			ins_record={"filename":kwargs["image_name"],"path":kwargs["path"],"latitude":lat,"longitude":longt,"treename":kwargs["treename"],"timestamp":kwargs["timestamp"],"owner":kwargs["owner"]}
			mDBTable.insert_one(ins_record)
		except Exception:
			 return Exception

		return "Saved successfuly"
	
	def search(self,**kwargs):
		mDBTable=self.mDB[kwargs["table_name"]]
		result=mDBTable.find()
		return result
		
	def retrieveAll(self,**kwargs):
		mDBTable=self.mDB[kwargs["table_name"]]
		allRecords= mDBTable.find()
		print allRecords
		return allRecords
	
