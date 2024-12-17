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
git clone git@github.com:MartinAmor04/sbd-tareafinal-1ev.git
```
### 2. Conectarse a Openstack a través de ssh o VPN:
```bash
ssh -J xuedua059@hadoop.cesga.es cesgaxuser@10.133.27.228
```
### 3. Copiar docker-compose:
Copia el contenido de docker-compose y pégalo en el nuevo archivo que creas con el editor de texto 'nano' dentor de la instancia
```bash
nano docker-compose.yml
```
### 4. Construir y Levantar los Servicios
Usa Docker Compose para construir y levantar el entorno completo:
```bash
docker-compose up -d
```
### 4. Verificar los Datos en MongoDBUsa Docker Compose para construir y levantar el entorno completo:
```bash
docker exec -it mongodb mongosh
```
Dentro del shell de MongoDB, selecciona la base de datos y revisa las colecciones:
```bash
use bicisCorunha
db.stations.find()
db.stations.countDocuments()
```
# Documentos almacenados durante las vacaciones

Durante el periodo de vacaciones, comprendido entre el **21 de diciembre** y el **8 de enero**, nuestro sistema realiza la recolección de datos con una frecuencia de **49 documentos cada 3 minutos**. Este cálculo asume un funcionamiento continuo las 24 horas del día.

## Cálculo

### Duración de las vacaciones
- **Del 21 al 31 de diciembre**: 11 días.  
- **Del 1 al 8 de enero**: 8 días.  
- **Total**: 19 días.

### Minutos totales
19 días × 24 horas/día × 60 minutos/hora = **27,360 minutos**

### Número de intervalos de recolección (cada 3 minutos)
27,360 minutos ÷ 3 minutos/intervalo = **9,120 intervalos**

### Documentos totales almacenados
9,120 intervalos × 49 documentos/intervalo = **446,880 documentos**

## Resultado
Durante el periodo de vacaciones, el sistema almacenará un total de **446,880 documentos**.

