# DOCUMENTACIÓN : SYS4PROJECTS-BACK

## DESCRIPCIÓN:
SYS4PROJECTS-BACK nos enlista los BOTS y a la vez nos muestra el estado en el que se encuentran, la ultima placa de la que recibio una señal y la hora-fecha en que esta fue recibida, para ello se consume información desde el REST-API que a la vez consume el API DE WIALON con el fin de mostrar la ultima placa recibida. Por otra parte, analiza la tabla "tb_status_bots" que se encuentra en la base de datos "db_api_bot" para mostrar el estado del bot y la fecha.

Esta API, también valida la existencia de un usuario y nos muestra los campos que contiene mediante una conexion a MONGODB.

## DEPLOYMENT:

EJECUTAR SCRIPT CON DOCKER: 

PASO 1 : Generar imagen con :

```docker build -t <nombre> .```

PASO 2 : Crear contenedor con la imagen :

```docker run -dp 3222:80 <nombre>```

## UBICACIÓN

SERVIDOR: 67.207.87.64

## BASE DE DATOS

### MYSQL

SERVER : 104.248.60.94

BD : db_api_bot

USER: root

PASS: Sys4Log$$sa