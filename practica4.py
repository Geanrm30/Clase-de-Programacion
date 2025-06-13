# Lector de Datos CSV - Ejercicio 4

# Abrir el archivo productos.csv en modo lectura y con codificación utf-8
with open('productos.csv', 'r', encoding='utf-8') as archivo:
    # Recorrer cada línea del archivo
    for linea in archivo:
        linea = linea.strip()  # Eliminar espacios y saltos de línea al final
        if not linea:
            continue  # Saltar líneas vacías
        partes = linea.split(',')  # Separar la línea en partes usando la coma
        if len(partes) != 4:
            print("Línea con formato incorrecto:", linea)  # Avisar si la línea no tiene 3 elementos
            continue
        numero, nombre, precio, cantidad = partes  # Asignar cada parte a una variable
        # Imprimir la información de forma ordenada
        print(f"{numero} | Producto: {nombre} | Precio: ${precio} | Stock: {cantidad} unidades")