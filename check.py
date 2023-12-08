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

def reach_profile(conn, profile, reach):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO reach_profile (name, reach) VALUES (%s, %s)", (profile, reach))

conn = conectar_a_mysql()
#prefijo
prefix = "https://www.instagram.com/"

try:
    df = obtener_datos_rango(conn)
    if len(sys.argv) > 1:
        link_enviado = sys.argv[1]
        if link_enviado.startswith(prefix):
            profile = link_enviado[len(prefix):].replace('/','')
        else:
            raise ValueError("sent link error")

    #Conexion con la Base de datos mediawaarde
    Value = link_value(conn, profile)
    for index, row in df.iterrows():
        lower_bound = row['FROM']
        upper_bound = row['TO'] if row['TO'] is not None else float('inf')

        if lower_bound <= Value < upper_bound:
            reach = row['Bedrag']
            reach_profile(conn, profile, reach)
            break
        elif Value >= 75000:
            reach = 3230
            reach_profile(conn, profile, reach)
            break
        
    else:
        raise ValueError("No se mando un link")

except mysql.connector.Error as e:
    print(f"Error en la base de datos: {e}")
finally:
    if conn.is_connected():
        conn.close()
