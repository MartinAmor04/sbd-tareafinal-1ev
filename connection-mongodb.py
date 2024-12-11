from pymongo import MongoClient
import requests
import time
client = MongoClient('mongodb://localhost:27017/')

db_name = client['bicisCorunha']
collection_name = db_name['stations']
def insert_data():
    url='http://api.citybik.es/v2/networks/bicicorunha'
    try:
        response=requests.get(url)
        data = response.json()
        stations=data.get('network',{}).get('stations',[])
        # print(stations)
        result = collection_name.insert_many(stations)
        print(f"Inserted {len(result.inserted_ids)} documents with IDs: {result.inserted_ids}")    
    except:
        print('Error: ',response.status_code)


intervalo=180

while True:
    insert_data()
    time.sleep(intervalo)