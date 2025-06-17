# Nombre del archivo donde se guardará la lista de compras
filename = "compras.txt"

# Abrir el archivo en modo escritura ('w') con codificación UTF-8
with open(filename, 'w', encoding='utf-8') as file:
    while True:
        # Solicitar al usuario que ingrese un producto
        producto = input("Ingresa un producto (o escribe 'fin' para terminar): ")
        # Si el usuario escribe 'fin', salir del ciclo
        if producto.lower() == "fin":
            break
        # Escribir el producto en el archivo, seguido de un salto de línea
        file.write(producto + "\n")

# Informar al usuario que la lista ha sido guardada
print("La lista de compras ha sido guardada en compras.txt")