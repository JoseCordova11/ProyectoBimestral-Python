print("Programa para convertir de grados centigrados a grados farenheit y a grados kelvin")
gc = 0
gf = 0
gk = 0

print("Ingrese los grados centigrados a convertir")
gc = float(input())

if gc > 0:
    gf = (gc * 9/5) + 32
    gk = gc + 273.15

    print(f"La equivalencia en grados farenheit es {gf}")
    print(f"La equivalencia en grados kelvin es {gk}")