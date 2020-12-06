print("Ejercicio 1")

limite = 100
j = 0

print("Ciclo For")
for i in range(limite+1):
    if i % 5 == 0:
        print(i)

print("\nCiclo While")

while True:
  if j % 5 == 0:
      print(j)
  j+=1
  if j>limite:
    break