from PIL import Image
import os
import subprocess
import sys

# Subprocess pwd
directory_process = subprocess.run(['pwd'], text=True, capture_output=True)
if directory_process.returncode == 0:
    actual_directory = directory_process.stdout.strip()
else:
    print('Error in pwd command')
    sys.exit(1)  # Salir si no se puede obtener el directorio actual

# Comprobar si se pasa la carpeta como argumento
if len(sys.argv) > 1:
    folder = sys.argv[1]
else:
    raise ValueError("Folder didn't send")

# Cambiar imagen a negativo
for file in os.listdir(folder):
    if file.endswith(".jpeg") and not "_negative" in file:
        path_file = os.path.join(folder, file)  # Usar 'folder' para obtener la ruta del archivo
        imagen = Image.open(path_file)
        negative = Image.eval(imagen, lambda x: 255 - x)
        negative_name = os.path.splitext(file)[0] + "_negative.jpeg"
        rute = os.path.join(folder, negative_name)  # Guardar la imagen negativa en la misma carpeta
        negative.save(rute)