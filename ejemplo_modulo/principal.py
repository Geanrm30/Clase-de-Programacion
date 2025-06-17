# Programa principal

# Importar modulo
import modulo as md
from modulo import dividir,suma,prod,mod

print("Programa con las operaciones basicas")
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
print(f"La resta es: {md.resta(num1,num2)}")
repuesta=dividir(num1,num2)
print("El resultado de dividir ",num1," y ",num2," es:", repuesta)
print(md.texto)
res=suma(num1,num2)
print("El resultado de sumar ",num1," y ",num2," es:", res)
print(f"La multiplicacion es: {md.prod(num1,num2)}")
print(f"El residuo de los numeros es: {md.mod(num1,num2)}")
