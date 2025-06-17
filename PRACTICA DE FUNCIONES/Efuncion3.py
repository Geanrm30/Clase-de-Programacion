#Calcular el promedio de 3 notas
def promedio(n1,n2,n3):
    resultado=(n1+n2+n3)/3
    return resultado

#Principal
print("Usando funciones en python")
nota1=int(input("Ingrese la primera nota:"))
nota2=int(input("Ingrese la segunda nota:"))
nota3=int(input("Ingrese la tercera nota:"))
total=promedio(nota1,nota2,nota3)
print(F"El promedio es:", total{2})