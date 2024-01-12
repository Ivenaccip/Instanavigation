import pandas as pd

# Cargar el archivo Excel
excel_file = pd.ExcelFile('X-mas.xlsx')

# Iterar sobre cada hoja del archivo Excel
for sheet_name in excel_file.sheet_names:
    # Leer la hoja actual en un DataFrame
    df_sheet = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Imprimir el contenido del DataFrame
    print(f"Contenido de la hoja '{sheet_name}':")
    print(df_sheet)
    print()