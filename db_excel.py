import pandas as pd
from openpyxl import Workbook
import sqlite3
from sqlalchemy import create_engine
import mysql.connector

#Mediawaarden
def datos_rango(cursor):
    cursor.execute("SELECT `van`, `tot`, `bedrag` FROM mediawaarde")
    df = pd.DataFrame(cursor.fetchall(), columns=['FROM', 'TO', 'Bedrag'])
    cursor.close()
    return df

#Hashtags
def hashtags(cursor):
    cursor.execute("SELECT `company`, `identificators` FROM companies")
    df_hashtags = pd.DataFrame(cursor.fetchall(), columns=['company', 'identificators'])
    cursor.close()
    return df_hashtags

#Id objects
def id_obj_down(cursor):
    query_id_obj = "SELECT Object_ID, Type, Link, Extract_text, Fecha, Profile FROM id_obj_download"
    cursor.execute(query_id_obj, create_engine)
    db_data = cursor.fetchall()
    cursor.close()
    return db_data

# Variables iniciales
information_xlsx = 'Information.xlsx'

conn = mysql.connector.connect(
#Conexion SQL
    host = 'localhost',
    user = 'office',
    password = 'Kroon111',
    database = 'alpha_test'
)

# Usando las funciones
cursor = conn.cursor()

df_hashtags = hashtags(cursor)
db_data = id_obj_down(cursor)
resultados_por_marca = {}

for marca, hashtags_brand in df_hashtags.iterrows():
    resultados_encontrados = []

    for record in db_data:
        texto, date, link = record
        
        for hashtag in hashtags_brand.dropna():
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