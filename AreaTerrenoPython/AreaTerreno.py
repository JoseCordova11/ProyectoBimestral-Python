print("Programa que permite calcular el area")

print("Ingrese el largo del rectangulo")
lr = float(input())

print("Ingrese la altura del triangulo")
at = float(input())

A = lr * at
B = (lr * at) / 2
area = A + B

print(f"El area del terreno es: {area}")
print(f"tiene un rectangulo de largo {lr} y un triangulo de altura {at}")
