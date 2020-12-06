def CalcularSerie(limite1):
    num = 0
    den = 3
    divisor = 1
    suma = 0
    primo = 0
    bandera = False

    for k in range(1, limite1 + 1):
        num = num + 1
        while not bandera:
            for i in range(1, primo + 1):
                if primo % i == 0:
                    divisor += 1
            if divisor == 2:
                den = primo
                primo += 1
                bandera = True
            else:
                primo = primo + 1
                bandera = False
            divisor = 0

        if k % 2 == 0:
            suma = suma - (num / den)
            print(f' - {num} / {den}', end=" ")
        else:
            suma = suma + (num / den)
            if k == 1:
                print(f'{num} / {den}', end=" ")
            else:

                print(f' + {num} / {den}', end=" ")

        bandera = False
    return suma


limite1 = int(input('Ingrese un límite:'))
print(' = ', CalcularSerie(limite1))