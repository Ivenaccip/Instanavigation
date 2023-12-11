import sqlite3
import os
import sys
from sqlalchemy import create_engine
import mysql.connector

def insert_into_db(conn, cursor, txt_file, data, profile_name):
    query = "INSERT INTO id_obj_download (Object_ID, Type, Name, Extract_text, Fecha, Profile) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (txt_file, "Post", *data, profile_name))
    conn.commit()

conn = mysql.connector.connect(
#Conexion SQL
    host = 'localhost',
    user = 'office',
    password = 'Kroon111',
    database = 'alpha_test'
)

# Usando las funciones
cursor = conn.cursor()

# Lista todos los archivos en el directorio actual con extensión .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt') and f != 'requirements.txt']

for txt_file in txt_files:
# Verifica si se recibió el argumento sql_profile
    if len(sys.argv) > 1:
        profile_name = sys.argv[1] 
    else:
        raise ValueError("Profile name was not sent")
    with open(txt_file, "r") as file:
        for line in file.readlines():
            data = line.strip().split(';')
            if len(data) == 3:
                insert_into_db(conn, cursor, txt_file, data, profile_name)

# Cerrar la conexión
cursor.close()
conn.close()

#Eliminacion de archivos .txt
for txt_file in txt_files:
    os.remove(txt_file)
