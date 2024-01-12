import pandas as pd
from sqlalchemy import create_engine
import sys
import glob
import os

# Datos de la base de datos
user = 'root'
password = 'Kroon111'
host = 'localhost'

# Hojas requeridas en los archivos Excel
required_sheets = ['Companies', 'Influencers', 'Mediawaarde', 'Sticker']

# Argumentos de línea de comandos
files = sys.argv[1:]
if len(files) == 0:
    raise ValueError("No se proporcionaron argumentos en la línea de comandos")

# Procesar cada prefijo de archivo pasado como argumento
for file_prefix in files:
    file_coincidence = glob.glob(f'{file_prefix}.xlsx')
    if not file_coincidence:
        print(f"No se encontraron archivos que coincidan con {file_prefix}")
        continue

    for excel_file_path in file_coincidence:
        # Ignorar archivos temporales que comienzan con '~$'
        if os.path.basename(excel_file_path).startswith('~$'):
            continue

        try:
            excel_file = pd.ExcelFile(excel_file_path, engine='openpyxl')
            missing_sheets = [sheet for sheet in required_sheets if sheet not in excel_file.sheet_names]
            if missing_sheets:
                print(f"Faltan las siguientes hojas en el archivo {excel_file_path}: {missing_sheets}")
                continue
            for sheet_name in excel_file.sheet_names:
                db_name = os.path.splitext(os.path.basename(file_prefix))[0]
                cadena_conexion = f'mysql+mysqlconnector://{user}:{password}@{host}/{db_name}'
                engine = create_engine(cadena_conexion)

                df_sheet = pd.read_excel(excel_file_path, sheet_name=sheet_name)
                if sheet_name == "Companies":
                    df_sheet.to_sql(f'{(sheet_name)}', con=engine, if_exists='append', index=False)
                
                if sheet_name == "Influencers":
                    df_sheet.to_sql(f'{(sheet_name)}', con=engine, if_exists='append', index=False)

                if sheet_name == "Mediawaarde":
                    # Reescribir columnas para que coincidan con las tablas de la base de datos
                    df_sheet.rename(columns={'Van': 'van', 'Tot volgers': 'tot', 'Bedrag': 'bedrag'}, inplace=True)
                    df_sheet.to_sql(f'{(sheet_name)}', con=engine, if_exists='append', index=False)

                if sheet_name == "Sticker":
                    df_sheet.to_sql(f'{(sheet_name)}', con=engine, if_exists='append', index=False)
        
        except Exception as e:
            print(f"Error al procesar el archivo {excel_file_path}: {e}")
            continue