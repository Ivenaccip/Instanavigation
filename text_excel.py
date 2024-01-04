import docx
import pandas as pd

# Leer el documento .docx
doc = docx.Document("Results.docx")
full_text = []

# Extraer el texto de cada párrafo
for para in doc.paragraphs:
    full_text.append(para.text)

# Procesar los datos
processed_data = []
for line in full_text:
    if line.strip():  # Asegurarse de que la línea no esté vacía
        parts = line.split()
        photo_number = parts[1]
        image_path = parts[2]
        detection = 'T' if 'Ketchup' in line else 'F'
        processed_data.append([photo_number, image_path, detection])

# Crear un DataFrame y exportarlo a Excel
df = pd.DataFrame(processed_data, columns=['Photo Number', 'Image', 'Detection'])
df.to_excel("Results.xlsx", index=False)