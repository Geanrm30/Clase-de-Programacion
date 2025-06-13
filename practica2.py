# Solicita al usuario el nombre del archivo de texto
filename = input("Introduce el nombre del archivo de texto: ")

try:
    # Intenta abrir el archivo en modo lectura con codificación UTF-8
    with open(filename, 'r', encoding='utf-8') as file:
        # Lee todas las líneas del archivo y las almacena en una lista
        lines = file.readlines()
        # Imprime la cantidad de líneas que tiene el archivo
        print(f"El archivo tiene {len(lines)} líneas.")
except FileNotFoundError:
    # Si el archivo no existe, muestra un mensaje de error
    print("Error: El archivo no existe. Por favor, verifica el nombre e inténtalo de nuevo.")