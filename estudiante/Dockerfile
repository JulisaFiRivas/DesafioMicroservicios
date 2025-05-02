# Usamos la imagen base de Python 3.9 (versión "slim" para ser más ligera)
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos todos los archivos desde el directorio actual 
COPY . .

# Instalamos las dependencias del proyecto desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto 3000 en el contenedor, que es donde la aplicación Flask escuchará
EXPOSE 3000

# Definimos el comando que se ejecutará cuando se inicie el contenedor
CMD ["python", "micro.py"]
