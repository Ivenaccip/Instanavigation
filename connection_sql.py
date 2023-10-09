import sqlite3

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
        date TEXT
    )
    ''')
    conn.commit()
    
    return conn, cursor

def insert_into_db(conn, cursor, data):
    cursor.execute("INSERT INTO posts (link, text, date) VALUES (?, ?, ?)", data)
    conn.commit()

# Usando las funciones
conn, cursor = connect_db('data_profiles.db')

with open("coffeewithalyss_clean.txt", "r") as file:
    for line in file.readlines():
        data = line.strip().split(';')
        if len(data) == 3:
            insert_into_db(conn, cursor, data)

# Cerrar la conexión
conn.close()
