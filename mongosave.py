import pymongo
from pymongo import MongoClient
import pdb
class mongosave:
	def __init__(self,dbname):
		mclient=MongoClient()
		self.mDB=mclient[dbname]
	
	def save_mongodb(self,**kwargs):
		try:
			pdb.set_trace()
			mDBTable=self.mDB[kwargs["table_name"]]
			ins_record={"filename":kwargs["image_name"],"path":kwargs["path"]}
			mDBTable.insert_one(ins_record)
		except Exception:
			 return Exception

		return "Saved successfuly"
	
	def search(self,**kwargs):
		mDBTable=mDB[kwargs["table_name"]]
		result=mDBTable.find()
		return result
		


