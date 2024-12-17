import requests
import time
from pymongo import MongoClient

# Configuración de la base de datos
MONGO_URI = 'mongodb://localhost:27017/'
DB_NAME = 'cheapshark'
COLLECTION_NAME = 'elden_ring'
API_URL = 'https://www.cheapshark.com/api/1.0/games?title=elden_ring'

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
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos de la API: {e}")
        return None


# Insertar datos en la colección de MongoDB
def insert_data(collection, data):
    if not data:
        print("No se encontraron videojuegos para insertar.")
        return
    for item in data:
        item["_id"] = item["gameID"]  # Usamos gameID como id
        try:
            collection.update_one(
                {"_id": item["_id"]},  # Filtro para evitar duplicados
                {"$set": item},        # Inserta o actualiza el documento
                upsert=True            # Crea el documento si no existe
            )
            print(f"Documento procesado: {item['_id']}")
        except Exception as e:
            print(f"Error al insertar el documento {item['_id']}: {e}")

# Código principal para ejecutar
if __name__ == "__main__":
    # Conectar a MongoDB
    collection = connect_to_mongo(MONGO_URI, DB_NAME, COLLECTION_NAME)

    # Intervalo para la inserción (en segundos)
    intervalo = 1800  

    # Bucle principal para insertar datos periódicamente
    while True:
        data = get_data(API_URL)
        
        if data is not None:
            print(f"Datos obtenidos: {len(data)}")
            insert_data(collection, data)
        else:
            print("No se pudieron obtener los datos de los videojuegos.")
        
        print(f"Esperando {intervalo} segundos antes de la próxima inserción...")
        time.sleep(intervalo)
