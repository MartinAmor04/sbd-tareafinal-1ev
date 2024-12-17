import pandas as pd
from pymongo import MongoClient
import pyarrow  
from urllib.parse import quote_plus


# Establece una conexión a MongoDB y devuelve la colección.
def connect_to_mongo(uri, db_name, collection_name):
    try:
        client = MongoClient(uri) # uri: URI de conexión a MongoDB
        db = client[db_name] # db_name: nombre de la base de datos
        collection = db[collection_name] # collection_name: nombre de la colección
        return collection
    except Exception as e:
        raise ConnectionError(f"Error al conectar con MongoDB: {e}")


# Exporta datos desde MongoDB a archivos CSV y Parquet.
def export_data(collection, output_csv, output_parquet):
    try:
        # Definición del pipeline de agregación
        pipeline = [
            {"$project": { 
                "_id": 0,
                "id": 1,
                "name": 1,
                "timestamp": 1,
                "free_bikes": 1,
                "empty_slots": 1,
                "uid": "$extra.uid",  # Alias para extraer campos anidados
                "last_updated": "$extra.last_updated",
                "slots": "$extra.slots",
                "normal_bikes": "$extra.normal_bikes",
                "ebikes": "$extra.ebikes"
            }}
        ]

        # Ejecución del pipeline
        data = collection.aggregate(pipeline) # collection: Objeto de la colección de MongoDB

        # Creación del DataFrame
        df = pd.DataFrame(data)

        if df.empty:
            print("Error: No se encontraron datos")
        else:
            print("Datos cargados correctamente.")
            print(df.info())

            # Exportación de archivos
            df.to_csv(output_csv, index=False) # Evita que el índice del DataFrame se incluya como una columna adicional en el archivo exportado
            print(f"Archivo CSV exportado: {output_csv}") # output_csv: Ruta para el archivo CSV

            df.to_parquet(output_parquet, index=False)
            print(f"Archivo Parquet exportado: {output_parquet}") #output_parquet: Ruta para el archivo Parquet

    except Exception as e:
        print(f"Error al exportar datos: {e}")

if __name__ == "__main__":
    # Configuración
    usuario = "xuedua059@hpc"
    contraseña = "ponercontraseña"

    # Escapa el nombre de usuario y la contraseña
    usuario_escapado = quote_plus(usuario)
    contraseña_escapada = quote_plus(contraseña)

    # Crea la URI con los valores escapados
    URI = f"mongodb://{usuario_escapado}:{contraseña_escapada}@10.133.27.228:27017/"
    DB_NAME = 'bicisCorunha'
    COLLECTION_NAME = 'stations'
    OUTPUT_CSV = './bicisCorunha.csv'
    OUTPUT_PARQUET = './bicisCorunha.parquet'

    try:
        # Conectar a MongoDB
        collection = connect_to_mongo(URI, DB_NAME, COLLECTION_NAME)
        # Exportar datos
        export_data(collection, OUTPUT_CSV, OUTPUT_PARQUET)
    except Exception as e:
        print(f"Error general: {e}")
