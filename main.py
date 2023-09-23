import argparse  
import pandas as pd 
import datetime  
import os 

# Función para obtener el nombre del archivo Excel a partir de su ruta
def obtener_nombre_archivo_excel(ruta_excel):
    return os.path.basename(ruta_excel)

# Función para generar el nombre del archivo de salida en el formato especificado
def obtener_nombre_archivo_salida(cic, seq):
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")
    return f"ABTPurchaseOrder_{formatted_datetime}_{cic}_{seq}.txt"

# Función para leer datos desde un archivo Excel
def leer_datos_desde_excel(ruta_excel):
    return pd.read_excel(ruta_excel)

# Función para escribir la cabecera en el archivo de salida
def escribir_cabecera_en_archivo(nombre_archivo):
    cabecera = """FH|ABTPurchaseOrderUploadv1.0|VTMAE|jacqueline.magana@airlinemro.parts|jacqueline.magana@airlinemro.parts|N|"""
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(cabecera + '\n')

# Función para escribir los resultados en el archivo de salida
def escribir_resultado_en_archivo(data_frame, nombre_archivo):
    with open(nombre_archivo, 'a') as archivo:
        for indice, fila in data_frame.iterrows():
            linea = f"HH|N|{fila['BlukNumbre']}|{fila['Status']}|{fila['Cage']}||{fila['PO']}|{fila['PartNumber']}|EA|{fila['Quantity']}|USD|20230517| || |VTMAE| ||||| |XXX|"
            archivo.write(linea + '\n')


def main():
    # Definir argumentos de línea de comandos
    parser = argparse.ArgumentParser(description='Convertir archivo Excel a formato especificado.')
    parser.add_argument('excel_file', help='Ruta del archivo Excel a procesar')
    args = parser.parse_args()

    # Obtener la ruta del archivo Excel desde los argumentos de línea de comandos
    ruta_excel = args.excel_file
    # Obtener el nombre del archivo Excel
    nombre_archivo_excel = obtener_nombre_archivo_excel(ruta_excel)

    # Configurar valores para CIC (Código de Identificación del Cliente) y SEQ (Número de secuencia)
    cic = "VTMAE"
    seq = 1

    # Generar el nombre del archivo de salida
    nombre_archivo_salida = obtener_nombre_archivo_salida(cic, seq)

    # Leer los datos desde el archivo Excel en un DataFrame de pandas
    df = leer_datos_desde_excel(ruta_excel)

    # Escribir la cabecera en el archivo de salida
    escribir_cabecera_en_archivo(nombre_archivo_salida)

    # Escribir los resultados en el archivo de salida
    escribir_resultado_en_archivo(df, nombre_archivo_salida)

    # Imprimir un mensaje de éxito
    print(f"La conversión se ha completado. El resultado se encuentra en '{nombre_archivo_salida}'.")

# Ejecutar la función principal si este script es el programa principal
if __name__ == "__main__":
    main()
