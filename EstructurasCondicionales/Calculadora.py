print("Calculadora")
print("Ingrese el primer numero")
num1 = float(input())
print("Ingrese el segundo numero")
num2 = float(input())

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
opc = int(input())


if opc == 1:
    total = num1 + num2
    print(f"La suma es: {total}")
if opc == 2:
    total = num1 - num2
    print(f"La resta es: {total}")
if opc == 3:
    total = num1 + num2
    print(f"La multiplicacion es: {total}")        
if opc == 4:
    total = num1 / num2
    print(f"La division es: {total}")
if opc >4:
    print("Opcion invalida")
