import pandas as pd
import datetime

# Datos de ejemplo
cic = "VTMAE"  # Código de Identificación del Cliente
current_datetime = datetime.datetime.now()
seq = 1  # Número de secuencia

# Formatear la fecha y hora según el formato especificado
formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")

# Crear el nombre del archivo
file_name = f"ABTPurchaseOrder_{formatted_datetime}_{cic}_{seq}.txt"

# Imprimir el nombre del archivo
print(file_name)




# Lee el archivo Excel
df = pd.read_excel('Libro.xlsx')

# Define la cabecera que deseas escribir en el archivo
cabecera = """FH|ABTPurchaseOrderUploadv1.0|VTMAE|jacqueline.magana@airlinemro.parts|jacqueline.magana@airlinemro.parts|N|"""

# Abre el archivo en modo escritura y escribe la cabecera
with open(file_name, 'w') as archivo:
    archivo.write(cabecera  + '\n')

print("Cabecera escrita en el archivo 'archivo.txt'.")

# Abre un archivo de texto para escribir el resultado
with open(file_name, 'a') as archivo:
    # Itera a través de las filas del DataFrame
    for indice, fila in df.iterrows():
        # Convierte los datos de la fila al formato deseado
        linea = f"HH|N|{fila['BlukNumbre']}|{fila['Status']}|{fila['Cage']}||{fila['PO']}|{fila['PartNumber']}|EA|{fila['Quantity']}|USD|20230517| || |VTMAE| ||||| |XXX|"
        # Escribe la línea en el archivo de resultado
        archivo.write(linea + '\n')

print("La conversión se ha completado. El resultado se encuentra en 'resultado.txt'.")
