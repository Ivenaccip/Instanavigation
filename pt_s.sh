#!/bin/bash

# Directorio donde se encuentran los archivos .pt
model_directory="/home/IA/model/yolov5/runs/train/exp/weights"

# Directorio de las imágenes
image_directory="/home/IA/model/yolov5/data/test_conf"

# Bucle para iterar sobre cada archivo .pt en el directorio
for model_file in "$model_directory"/*.pt; do
    echo "Ejecutando el modelo: $model_file"
    python3 detect.py --weights "$model_file" --img 640 --conf 0.20 --source "$image_directory" --save-csv
done
