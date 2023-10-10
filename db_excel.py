import pandas as pd
from openpyxl import Workbook
import sqlite3

# Variables iniciales
information_xlsx = 'Information.xlsx'
db_name = 'data_profiles.db'

# Leer hashtags y límites desde Information.xlsx
df_hashtags = pd.read_excel(information_xlsx, sheet_name='hashtags', index_col=0)
limits_df = pd.read_excel(information_xlsx, sheet_name='media_value')

limits_df['From'] = pd.to_numeric(limits_df['From'], errors='coerce')
limits_df['To'] = pd.to_numeric(limits_df['To'], errors='coerce')

# Conexión con la base de datos
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Obtener todos los registros de la base de datos
cursor.execute("SELECT text, date, link FROM posts")
db_data = cursor.fetchall()

resultados_por_marca = {}

for marca, hashtags in df_hashtags.iterrows():
    resultados_encontrados = []

    for record in db_data:
        texto, date, link = record
        for hashtag in hashtags.dropna():
            if hashtag in texto:
                reward = None
                # Omitimos la parte que verifica el Reach porque mencionaste ignorarlo
                resultados_encontrados.append((texto, date, link, reward))

    resultados_por_marca[marca] = resultados_encontrados

# Crear un archivo Excel de salida y hojas de cálculo con nombres de archivo y marca
output_filename = 'Results.xlsx'
workbook = Workbook()

for marca, resultados in resultados_por_marca.items():
    worksheet = workbook.create_sheet(title=f'{marca}')
    worksheet.append(["Text", "Time", "Link", "Reward"])  # Agregar la primera fila con encabezados

    for idx, (texto, date, link, reward) in enumerate(resultados, start=2):  # Comenzar desde la fila 2 para los datos
        worksheet.cell(row=idx, column=1, value=texto)
        worksheet.cell(row=idx, column=2, value=date)
        worksheet.cell(row=idx, column=3, value=link)
        worksheet.cell(row=idx, column=4, value=reward)

# Guardar el archivo Excel
workbook.remove(workbook['Sheet'])  # Eliminar la hoja en blanco predeterminada
workbook.save(output_filename)