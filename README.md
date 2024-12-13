# SBD-TareaFinal-1EV

Este repositorio contiene un sistema basado en Docker Compose para gestionar datos de las estaciones de bicicletas en Coruña. El sistema consta de dos servicios principales:

1. **MongoDB**: Una base de datos donde se almacenan los datos.
2. **Get-from-API**: Un servicio Python que extrae información de la API de CitiBike y la guarda en MongoDB.

## 🛠️ Requisitos

Asegúrate de tener instalados:

- **Docker** 

---

## 🚀 Uso del Proyecto

### 1. Clonar el Repositorio

```bash
git@github.com:MartinAmor04/SBD-TareaFinal-1EV.git
```
### 2. Construir y Levantar los Servicios
Usa Docker Compose para construir y levantar el entorno completo:
```bash
docker-compose up -d
```
### 3. Verificar los Datos en MongoDBUsa Docker Compose para construir y levantar el entorno completo:
```bash
docker exec -it mongodb mongosh
```
Dentro del shell de MongoDB, selecciona la base de datos y revisa las colecciones:
```bash
use bicisCorunha
db.stations.find()
```

