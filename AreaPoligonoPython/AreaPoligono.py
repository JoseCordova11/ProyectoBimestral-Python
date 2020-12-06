
print("Programa para calcular area de un poligono")
print("")

print("Ingrese el lado del cuadrado")
lc = float(input())

print("Ingrese la altura del triangulo")
at = float(input())

print("Ingrese la altura del rectangulo")
ar = float(input())


A =  pow(lc, 2)
B = (lc + at) / 2
ats = B * 3
D = lc + ar
area = A + ats + D 

print(f"El area del poligono compuesto es: {area}")
print(f"compuesto por un cuadrado de lado {lc} , un rectangulo de altura {ar} y un triangulo de altura {at}")
        
