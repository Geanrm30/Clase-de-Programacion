# ELiminar lineas de archivos
# Abrir el archivo y leer lineas
with open("datos.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

#filtrar las lineas que no contienen "Segunda linea"
lineas_filtradas = [linea for linea in lineas if linea.strip() != "Segunda linea"]

#sobreescribir el archivo con las lineas filtradas
with open("datos.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas_filtradas)