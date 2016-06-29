#from flask_pymongo import PyMongo
import requests

import time
import base64
import pdb

imgData=""
with open("audience.jpg", "rb") as imageFile:
    imgData = base64.b64encode(imageFile.read())

payload={'id':time.time(),'image':imgData}
resp= requests.post('http://localhost:5000/savedata', data = payload)

