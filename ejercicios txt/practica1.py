import datetime

# Obtener fecha y hora actual
fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Solicitar entrada al usuario
entrada = input("Escribe tu entrada para el diario: ")

# Abrir el archivo en modo de adición
with open("diario.txt", "a", encoding="utf-8") as archivo:
    # Escribir fecha, hora y entrada
    archivo.write(f"{fecha_hora} - {entrada}\n")

# Mensaje de confirmación
print("Tu entrada ha sido guardada en el diario.")