# DesafioMicroservicios
Desafío de implementar 3 microservicios con Docker compose

## Estructura del Proyecto
desafriomicroservicios/
estudiante/
   micro.py
   Dockerfile
   requirements.txt
evaluacion/
   micro.py
   Dockerfile
   requirements.txt
   init.sql
docker-compose.yml

## Requisitos Previos

Antes de empezar, asegúrate de tener instalados los siguientes programas en tu máquina:

- [Docker](https://www.docker.com/get-started) (incluye Docker Compose)
- [Python](https://www.python.org/downloads/) 3.9 o superior

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://tu-repositorio.git
   cd tu-repositorio
   
## APIS
Microservicio de Estudiante:
http://localhost:3000/estudiante

Microservicio de Evaluación:
http://localhost:4000/evaluacion

## Ejecutar
El proyecto debe ser ejecutado con el comando docker compose up -d –build 

## ejemplo de peticion 
estudainte
{
  "rut": "12345678-9",
  "nombre": "Ana",
  "carrera": "Ingeniería"
}

evaluacion 
{
  "rut": "12345678-9",
  "semestre": "2024-1",
  "asignatura": "Bases de Datos",
  "nota": 6.5
}
