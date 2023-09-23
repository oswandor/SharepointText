import argparse
import datetime
from shareplum import Site, Office365

def obtener_datos_de_sharepoint(sitio, lista):
    # Autenticación en SharePoint
    authcookie = Office365(sitio, username='william.castillo@airlinemro.parts', password='WeCd620036801740682015$WXP7').GetCookies()
    sitio_sharepoint = Site(sitio, authcookie=authcookie)

    # Obtener la lista de SharePoint
    lista_sharepoint = sitio_sharepoint.List(lista)

    # Obtener todos los elementos de la lista
    elementos = lista_sharepoint.GetListItems()

    return elementos

def obtener_nombre_archivo_salida(cic, seq):
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")
    return f"ABTPurchaseOrder_{formatted_datetime}_{cic}_{seq}.txt"

def escribir_resultado_en_archivo(elementos, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for elemento in elementos:
            # Ajusta el formato de los datos según sea necesario
            linea = f"HH|N|{elemento['BlukNumbre']}|{elemento['Status']}|{elemento['Cage']}||{elemento['PO']}|{elemento['PartNumber']}|EA|{elemento['Quantity']}|USD|20230517| || |VTMAE| ||||| |XXX|"
            archivo.write(linea + '\n')

def main():
    parser = argparse.ArgumentParser(description='Convertir datos de una lista de SharePoint a formato especificado.')
    parser.add_argument('sitio_sharepoint', help='URL del sitio de SharePoint')
    parser.add_argument('lista_sharepoint', help='Nombre de la lista de SharePoint')
    args = parser.parse_args()

    sitio = args.sitio_sharepoint
    lista = args.lista_sharepoint

    cic = "VTMAE"
    seq = 1
    nombre_archivo_salida = obtener_nombre_archivo_salida(cic, seq)

    elementos = obtener_datos_de_sharepoint(sitio, lista)

    escribir_resultado_en_archivo(elementos, nombre_archivo_salida)

    print(f"La conversión se ha completado. El resultado se encuentra en '{nombre_archivo_salida}'.")

if __name__ == "__main__":
    main()
