print("Programa que determina cual es el mayor de 3 números")

print("Ingrese 3 números")
n1 = float(input())
n2 = float(input())
n3 = float(input())

if (n1 > n2 and n1 > n3) :
    print(f"El mayor numero es: {n1}")
else:
    if (n2 > n1 and n2 > n3):
        print(f"El mayor numero es: {n2}")
    else:
        print(f"El mayor numero es: {n3}")



        