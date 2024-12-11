# ! pip install pymongo[srv]==4.6.2
# ! pip install requests

from pymongo import MongoClient
import time
import requests

class AtlasClient ():

   def __init__ (self, altas_uri, dbname):
       self.mongodb_client = MongoClient(altas_uri)
       self.database = self.mongodb_client[dbname]

   ## Comprobobamos la conexión
   def ping (self):
       self.mongodb_client.admin.command('ping')

   def get_collection (self, collection_name):
       collection = self.database[collection_name]
       return collection

   def find (self, collection_name, filter = {}, limit=0):
       collection = self.database[collection_name]
       items = list(collection.find(filter=filter, limit=limit))
       return items

ATLAS_URI = 'mongodb+srv://admin:admin@citybik-cluster.2wdih.mongodb.net/?retryWrites=true&w=majority&appName=CityBik-Cluster'

DB_NAME = 'bicisCoruña'
COLLECTION_NAME = 'info'

atlas_client = AtlasClient (ATLAS_URI, DB_NAME)
atlas_client.ping()
print ('Connected to Atlas instance! We are good to go!')

# Conexión al cliente de MongoDB
client = MongoClient(ATLAS_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def insert_data():
    url='http://api.citybik.es/v2/networks/bicicorunha'
    try:
        response=requests.get(url)
        data = response.json()
        result = collection.insert_one(data)
        print(f"Inserted document with ID: {result.inserted_id}")    
    except:
        print('Error: ',response.status_code)


intervalo=60

while True:
    insert_data()
    time.sleep(intervalo)