import sqlite3
import os

def connect_db(db_name):
    # Conectarse a la base de datos (la crea si no existe)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Crear la tabla (si no existe)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        link TEXT,
        text TEXT,
        date TEXT,
        profile TEXT
    )
    ''')
    conn.commit()
    
    return conn, cursor

def insert_into_db(conn, cursor, data, profile_name):
    cursor.execute("INSERT INTO posts (link, text, date, profile) VALUES (?, ?, ?, ?)", (*data, profile_name))
    conn.commit()

# Usando las funciones
conn, cursor = connect_db('data_profiles.db')

# Lista todos los archivos en el directorio actual con extensión .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt') and f != 'requirements.txt']

for txt_file in txt_files:
    profile_name = txt_file.replace("_clean.txt", "")
    with open(txt_file, "r") as file:
        for line in file.readlines():
            data = line.strip().split(';')
            if len(data) == 3:
                insert_into_db(conn, cursor, data, profile_name)

# Cerrar la conexión
conn.close()

#Eliminacion de archivos .txt
for txt_file in txt_files:
    os.remove(txt_file)
