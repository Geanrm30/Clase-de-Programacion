# Ejemplo de escritura de un archivo de texto con codificación UTF-8
arch1 = open("datos2.txt", "w", encoding="utf-8")
arch1.write("Primer línea.\n")
arch1.write("Segunda línea.\n")
arch1.write("Tercer línea.\n")
arch1.write("♪")  # Alt+269
arch1.close()