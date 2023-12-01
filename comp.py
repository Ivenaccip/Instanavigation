import mysql.connector
import os
import re

def connect_db(db_name):
    # Conectarse a la base de datos MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='office',
        password='Kroon111',
        database=db_name
    )
    cursor = conn.cursor()
    
    # Crear la tabla (si no existe)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        identifier INT,
        link TEXT,
        text TEXT,
        date TEXT,
        profile TEXT
    )
    ''')
    conn.commit()
    
    return conn, cursor

def insert_into_db(conn, cursor, data, profile_name, identifier):
    cursor.execute("INSERT INTO posts (identifier, link, text, date, profile) VALUES (%s, %s, %s, %s, %s)", (identifier, *data, profile_name))
    conn.commit()

def get_profile_name_by_identifier(conn, identifier):
    cursor = conn.cursor()
    cursor.execute("SELECT profile FROM posts WHERE identifier = %s", (identifier,))
    result = cursor.fetchone()
    return result[0] if result else None

# Usando las funciones
conn, cursor = connect_db('alpha_test')

# Lista todos los archivos en el directorio actual con extensión .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt') and f != 'requirements.txt']

for txt_file in txt_files:
    # Extraer el identificador del nombre del archivo
    identifier = int(re.search(r'data_(\d+).txt', txt_file).group(1))
    profile_name = f"profile_{identifier}"  # O cualquier otra lógica para obtener el profile_name

    with open(txt_file, "r") as file:
        for line in file.readlines():
            data = line.strip().split(';')
            if len(data) == 3:
                insert_into_db(conn, cursor, data, profile_name, identifier)

# Usar el identificador para obtener el profile_name
# Aquí puedes cambiar el identificador para probar con diferentes archivos
test_identifier = 1
profile_name = get_profile_name_by_identifier(conn, test_identifier)
print(f"El profile_name para el identificador {test_identifier} es {profile_name}")

# Cerrar la conexión
conn.close()

# Eliminación de archivos .txt
for txt_file in txt_files:
    os.remove(txt_file)
