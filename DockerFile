# Usa la imagen base de Python
FROM python:3.12-slim

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias usando pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia los archivos Python al contenedor
COPY connection-mongodb.py .
COPY reader-mongodb.py .

# Define el comando por defecto que ejecutará los scripts Python
CMD ["sh", "-c", "python connection-mongodb.py && python reader-mongodb.py"]
