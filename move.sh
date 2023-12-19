#!/bin/bash

#Data for MySQL
BD_USER='office'
BD_PASS='Kroon111'
BD_NAME='alpha_test'
BD_HOST='localhost'

# Definir las variables
user="kroonadmin"
origin="/home/${user}/Downloads"
destination=$(pwd)

# Obtener la fecha actual en el formato deseado
today=$(date +"%Y-%m-%d")

# Crear una subcarpeta con la fecha de hoy dentro del destino
destination_folder="${destination}/${today}"
mkdir -p "${destination_folder}"

# Mover todos los archivos .jpeg del origen a la carpeta de destino con la fecha de hoy
mv "${origin}"/*.jpeg "${destination_folder}/"

# Aplicar Tesseract OCR a cada imagen en la carpeta de destino
for imagen in "${destination_folder}"/*.jpeg; do
    # Verificar si el archivo es una imagen
    if [[ -f "$imagen" ]]; then
        # Extraer el nombre base del archivo sin la extensión
        nombre_base=$(basename "$imagen" .jpeg)

        # Usar Tesseract para convertir la imagen a texto
        tesseract "$imagen" "${destination_folder}/${nombre_base}_texto" -l eng

        echo "Texto extraído de $imagen guardado en ${nombre_base}_text.txt"
    fi
done
