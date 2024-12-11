import pandas as pd
from pymongo import MongoClient
import pyarrow

client = MongoClient('mongodb://localhost:27017/')

db_name = client['bicisCorunha']
collection_name = db_name['stations']
def export_data():
    pipeline = [
        {"$project": { 
            "_id":0,
            "id": 1,
            "name": 1,
            "timestamp": 1,
            "free_bikes": 1,
            "empty_slots": 1,
            "extra.uid": 1,  
            "last_updated": 1,
            "slots": 1,
            "normal_bikes": 1,
            "ebikes": 1
        }}
    ]
    data=collection_name.aggregate(pipeline)
    df=pd.DataFrame(data)
    print(df)
    df.to_csv('../bicisCorunha.csv')
    df.to_parquet('../bicisCorunha.parquet')

export_data()

