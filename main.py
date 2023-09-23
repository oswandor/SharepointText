import argparse
import pandas as pd
import datetime
import os

def obtener_nombre_archivo_excel(ruta_excel):
    return os.path.basename(ruta_excel)

def obtener_nombre_archivo_salida(cic, seq):
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")
    return f"ABTPurchaseOrder_{formatted_datetime}_{cic}_{seq}.txt"

def leer_datos_desde_excel(ruta_excel):
    return pd.read_excel(ruta_excel)

def escribir_cabecera_en_archivo(nombre_archivo):
    cabecera = """FH|ABTPurchaseOrderUploadv1.0|VTMAE|jacqueline.magana@airlinemro.parts|jacqueline.magana@airlinemro.parts|N|"""
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(cabecera + '\n')

def escribir_resultado_en_archivo(data_frame, nombre_archivo):
    with open(nombre_archivo, 'a') as archivo:
        for indice, fila in data_frame.iterrows():
            linea = f"HH|N|{fila['BlukNumbre']}|{fila['Status']}|{fila['Cage']}||{fila['PO']}|{fila['PartNumber']}|EA|{fila['Quantity']}|USD|20230517| || |VTMAE| ||||| |XXX|"
            archivo.write(linea + '\n')

def main():
    parser = argparse.ArgumentParser(description='Convertir archivo Excel a formato especificado.')
    parser.add_argument('excel_file', help='Ruta del archivo Excel a procesar')
    args = parser.parse_args()

    ruta_excel = args.excel_file
    nombre_archivo_excel = obtener_nombre_archivo_excel(ruta_excel)

    cic = "VTMAE"
    seq = 1
    nombre_archivo_salida = obtener_nombre_archivo_salida(cic, seq)

    df = leer_datos_desde_excel(ruta_excel)

    escribir_cabecera_en_archivo(nombre_archivo_salida)
    escribir_resultado_en_archivo(df, nombre_archivo_salida)

    print(f"La conversión se ha completado. El resultado se encuentra en '{nombre_archivo_salida}'.")

if __name__ == "__main__":
    main()
