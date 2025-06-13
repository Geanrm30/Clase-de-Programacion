# Ejemplificar lectura de un archivo de texto

# Crear la variable para manipular el archivo
archi1= open("datos.txt", "r")
contenido = archi1.read()
print(contenido)
archi1.close()