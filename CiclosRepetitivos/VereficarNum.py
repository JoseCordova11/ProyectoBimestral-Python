print(" ")
print("Programa para vereficar un numero")
print("Ingrese el limite del número a verificar")
limite = int(input())

i = 0 
num = 0
sumPar = 0
sumImpar = 0
sumNeg = 0
sumPos = 0



while i <= limite:
    print("Ingrese el número a verificar")
    num = int(input())
    if num % 2 == 0:
        sumPar = sumPar + num
    else:
        sumImpar = sumImpar + num
    if num > 0:
        sumPos = sumPos + num     
    else:
        sumNeg = sumNeg + num      
    i = i + 1

    print(f"La suma de los pares es: {sumPar}")
    print(f"La suma de los impares es: {sumImpar}")       
    print(f"La suma de los positivos es: {sumPos}")  
    print(f"La suma de los negativos es: {sumNeg}")



