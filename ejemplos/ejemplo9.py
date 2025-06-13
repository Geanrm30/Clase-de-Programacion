# Solicitando datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
salario = input("Ingresa tu salario: ")

# Formatear los datos en una linea
linea = f"{nombre},{apellido},{edad},{salario}\n"

# Guardar datos en un archivo especificado por el usuario
ruta = input("Nombre del archivo donde guardar los datos: ")
with open(ruta, "a") as archivo:
    archivo.write(linea)
    archivo.write("Primera linea \n")
    archivo.write("Segunda linea \n")
    archivo.write("Tercera linea \n")

print("Datos guardados correctamente")
print("Fin del programa")