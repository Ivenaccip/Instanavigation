import mysql.connector
import pandas as pd

def conectar_a_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="office",
        password="Kroon111",
        database="alpha_test"
    )

def obtener_datos_rango(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT `van`, `tot`, `bedrag` FROM mediawaarde")
    df = pd.DataFrame(cursor.fetchall(), columns=['FROM', 'TO', 'Bedrag'])
    cursor.close()
    return df

conn = conectar_a_mysql()

try:
    df = obtener_datos_rango(conn)
    Value = 80000

    for index, row in df.iterrows():
        upper_bound = row['TO'] if row['TO'] is not None else float('inf')
        # Ajusta la condición para ser exclusiva en el límite superior
        if row['FROM'] <= Value < upper_bound:
            print(f"{row['Bedrag']}")
            break  # Detiene el bucle después de encontrar el primer valor coincidente

except mysql.connector.Error as e:
    print(f"Error en la base de datos: {e}")
finally:
    if conn.is_connected():
        conn.close()
