print("Programa para verificar is un numero es par o impar")

print("Ingrese el numero a verificar")
num = int(input())

if num % 2 == 0 :
    tipo = "Par"
else :
    tipo = "Impar"

print(f"El numero {num} es {tipo}")
