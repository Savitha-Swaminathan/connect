

from pymongo import MongoClient
client=MongoClient("mongodb://192.168.1.154:27017")
MongoClient_connect = True
if MongoClient_connect==True:
   print("Its connected to MongoDB")
else:
   print("its not connected to MongoDB")
client.close()
