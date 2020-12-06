print("Ejercicio 3")

suma = 0
Nvalores = 0
print('Ingrese distintos valores: ')
while (suma < 10000):
    j = int(input())
    if j == 0:
        print('Ingresa un valor mayor a 0.')
    elif j > 10000:
        print('Ingresa un valor menor a 10000')
    suma = j + suma
    Nvalores +=1

media = suma / Nvalores
print(f'Ingresaste {Nvalores} números.')
print(f'La media es: ', media)
print(f'La suma de los valores ingresados es: ', suma)