print("Ciclos Repetitivos")
print("Ingrese el limite de números a presentar")
n = int(input())

i = 1 
suma = 0

while (i <= n):
    print(i)
    suma = suma + i
    i = i + 1

print(f"La suma de los numeros es: {suma}")
