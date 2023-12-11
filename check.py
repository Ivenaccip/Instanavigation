import mysql.connector
import pandas as pd
import sys

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

def link_value(conn, profile):
    cursor = conn.cursor()
    cursor.execute(f"SELECT `reach` FROM actual_reach WHERE name = %s", (profile,))
    Value = cursor.fetchone()
    return Value[0] if Value else None

def reach_profile(conn, profile, mediawaarde):
    cursor = conn.cursor()
    update_mediawaarde = (f"UPDATE reach_profile SET mediawaarde = %s WHERE name = %s")
    cursor.execute(update_mediawaarde, (mediawaarde, profile))

conn = conectar_a_mysql()

try:
    df = obtener_datos_rango(conn)
    if len(sys.argv) > 1:
        profile = sys.argv[1]

    #Conexion con la Base de datos mediawaarde
    Value = link_value(conn, profile)
    for index, row in df.iterrows():
        lower_bound = row['FROM']
        upper_bound = row['TO'] if row['TO'] is not None else float('inf')

        if lower_bound <= Value < upper_bound:
            mediawaarde = row['Bedrag']
            reach_profile(conn, mediawaarde, profile)
            break
        elif Value >= 75000:
            mediawaarde = 3230
            reach_profile(conn, mediawaarde, profile)
            break
        
    else:
        raise ValueError("No se mando un link")

except mysql.connector.Error as e:
    print(f"Error en la base de datos: {e}")
finally:
    if conn.is_connected():
        conn.close()
