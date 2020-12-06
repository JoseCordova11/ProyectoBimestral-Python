print("Ingrese el linite de números a verificar si son primos")
limite = int(input())

i = 1
i1 = 1 
divisor = 0

while i <= limite:
    print("Ingrese el numero a verificar")
    num = int(input())

    while i1 <= limite:
        if num % i1 == 0:
            divisor = divisor + 1 
        i1 = i1 + 1 

    if divisor == 2:
        print(f"{num} es primo")
        print("--------")
    else:
        print(f"{num} no es primo")

    i1 = 1
    divisor = 0 
    i = i + 1                 