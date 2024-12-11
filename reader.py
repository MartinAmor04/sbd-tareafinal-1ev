# ! pip install pymongo[srv]==4.6.2
# ! pip install requests

from pymongo import MongoClient
import time
import requests
import pandas as pd

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

   def find(self, collection_name, filter={}, projection=None, limit=0):
        collection = self.get_collection(collection_name)
        items = list(collection.find(filter=filter, projection=projection, limit=limit))
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

def export_data():
    alldata=atlas_client.find(collection_name=COLLECTION_NAME,projection={
            "network.stations.id": 1,
            "network.stations.name": 1,
            "network.stations.timestamp": 1,
            "network.stations.free_bikes": 1,
            "network.stations.empty_slots": 1,
            "network.stations.extra.uid": 1,
            "network.stations.extra.last_updated": 1,
            "network.stations.extra.slots": 1,
            "network.stations.extra.normal_bikes": 1,
            "network.stations.extra.ebikes": 1,
            "_id": 0
        })
    # print(alldata)
    print(type(alldata))
    df=pd.DataFrame(alldata)
    print(df)


def print_sample_document():
    sample = atlas_client.find(collection_name=COLLECTION_NAME, limit=1)
    if sample:
        print("Ejemplo de documento:", sample[0])
    else:
        print("No se encontraron documentos.")

#print_sample_document()

export_data()
