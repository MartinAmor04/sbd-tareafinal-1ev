import requests
import time
from pymongo import MongoClient

# Configuración de la base de datos
MONGO_URI = 'mongodb://localhost:27017/'
DB_NAME = 'bicisCorunha'
COLLECTION_NAME = 'stations'
API_URL = 'http://api.citybik.es/v2/networks/bicicorunha'

# Establece conexión con MongoDB y devuelve la colección
def connect_to_mongo(uri, db_name, collection_name):
    try:
        client = MongoClient(uri) # uri: URI de conexión de MongoDB
        db = client[db_name] # db_name: Nombre de la base de datos
        collection = db[collection_name] # collection_name: Nombre de la colección
        return collection
    except Exception as e:
        print(f"Error de conexión a MongoDB: {e}")
        raise

# Realiza una solicitud GET a la API para obtener la información de las estaciones.
def get_data(url):
    try:
        response = requests.get(url) # url: URL de la API de CityBikes
        response.raise_for_status()  # Lanza un error para respuestas de error HTTP (4xx, 5xx)
        data = response.json()
        stations = data.get('network', {}).get('stations', [])
        return stations
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos de la API: {e}")
        return None


# Insertar datos en la colección de MongoDB
def insert_data(collection, stations):
    if not stations:
        print("No se encontraron estaciones para insertar.")
        return
    try:
        result = collection.insert_many(stations) 
        print(f"Se insertaron {len(result.inserted_ids)} documentos con IDs: {result.inserted_ids}")
    except Exception as e:
        print(f"Error al insertar los datos en MongoDB: {e}")

# Código principal para ejecutar
if __name__ == "__main__":
    # Conectar a MongoDB
    collection = connect_to_mongo(MONGO_URI, DB_NAME, COLLECTION_NAME)

    # Intervalo para la inserción (en segundos)
    intervalo = 180  

    # Bucle principal para insertar datos periódicamente
    while True:
        stations = get_data(API_URL)
        
        if stations is not None:
            print(f"Datos obtenidos: {len(stations)} estaciones.")
            insert_data(collection, stations)
        else:
            print("No se pudieron obtener los datos de las estaciones.")
        
        print(f"Esperando {intervalo} segundos antes de la próxima inserción...")
        time.sleep(intervalo)
