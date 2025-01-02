![dalle](https://github.com/user-attachments/assets/4d525d5b-5043-44fc-a48c-832dcd31b2cf)

# Repositorio del Trabajo de Final de Master de Víctor Cáncer Castillo

Este repositorio contiene los notebooks y scripts de Python utilizados durante el desarrollo del proyecto en el marco del Trabajo de Final de Master de la UOC para el Máster de Ciencia de Datos.

En este proyecto se utilizan los modelos de YOLOv5 y YOLOv11 desarrollados por Ultralytics. 

La ejecución de los notebooks se ha realizado en Google Colabs con Google Drive como sistema de almacenaje. Se debe montar Google Drive en Google Colab para poder reproducir los resultados.

## Notebooks

En la carpeta de _notebooks_ encontramos los cuadernos de Jupyter utilizados durante el proyecto. 

Tanto para el modelo YOLOv5 como para YOLOv11 encontramos tres tipos de cuaderno: 
* **Entrenamiento**: Un cuaderno que nos permite enternar el modelo con uno o más datasets.
* **Validación**: Un cuaderno que nos permite validar un modelo _custom_ contra el dataset que queramos.
* **Integración de nuevos datos**: Un cuaderno que nos permite integrar nuevos datos a nuestro modelo para mejorarlo.
* **Predicciones**: Un cuaderno para hacer predicciones de la ubicación de las tortugas tanto en video (para la version 11) como para imágenes (para ambas versiones).

## Scripts de Python

Durante el proyecto se ejecutaron algunos scripts de Python para pequeños procesos que se podían ejecutar en local:
* **generador_dataset_Bahamas.py**: Genera las imágenes y normalizan las etiquetas a partir de los videos de Bahamas.
* **plot_tallas.py**: Sirve para crear el gráfico final de los resultados con las diferentes tallas de YOLO.
* **remove_extra_column.py**: Se elimina la última columna de un fichero de etiquetas por una columna de más que hay en algunas etiquetas.
* **visualizar_etiquetas.py**: Se utiliza para visualizar las etiquetas sobre las imágenes de los datasets.

## Ficheros de parámetros

Se adjuntan los siguientes ficheros YAML al repositorio: 
* **DELT.yaml** - Fichero que define las carpetas de entorno así como las clases de YOLO (en este caso solo una: la tortuga).
* **DELT_validation.yaml** - Fichero que define las carpetas de entorno así como las clases de YOLO (en este caso solo una: la tortuga). Este fichero se utiliza en el notebook de "Integración de nuevos datos".
* **DELTv11.yaml** - Fichero que define las carpetas de entorno así como las clases de YOLO (en este caso solo una: la tortuga).
* **DELTv11_validation.yaml** - Fichero que define las carpetas de entorno así como las clases de YOLO (en este caso solo una: la tortuga). Este fichero se utiliza en el notebook de "Integración de nuevos datos".

No se adjunta el fichero **.comet.config** ya que contiene una clave API privada, se debe crear una cuenta en [Comet](https://www.comet.com/site/) de manera gratuita para conseguir una clave API.

> [!NOTE]
> La imagen de portada se ha generado utilizando DALL-E, de OpenAI
