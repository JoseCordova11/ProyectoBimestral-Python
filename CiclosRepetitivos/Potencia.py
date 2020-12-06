print("Ciclo para una Potencia")

i = 1
resul = 1 

print("Ingrese la base de la potencia")
base = int(input())
print("Ingresar la potencia")
pot = int(input())

while (i <= pot):
    resul = resul * base 
    i = i + 1 

print(f"La potencia de: {base} elevado a: {pot} es: {resul}")




    
