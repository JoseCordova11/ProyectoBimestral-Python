print("Serie Fibonacci con ciclo For")
print("Ingrese el limite de la serie")
limite = int(input())
i = 1
a = 0
b = 1
if limite % 2 == 0:
    print(int(limite/2))
    for i in range(i, int(limite/2)+i):
        print(a)
        print(b)
        a = a + b
        b = a + b
else:
    i = i - 2
    print(a)
    a = 1

    for i in range(int(i + limite/2), int(limite)-2):
        print(a)
        print(b)
        a = a + b
        b = a + b