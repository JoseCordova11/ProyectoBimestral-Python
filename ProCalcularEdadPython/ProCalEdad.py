print(" ")
print("Programa para calcular la edad en dia, meses y años")
print("Ingrese su año de nacimiento")
an = int(input())
print("Ingrese su mes de nacimiento")
mn = int(input())
print("Ingrese su dia de nacimiento")
dn = int(input())
print("Ingrese el año actual")
aa = int(input())
print("Ingrese el mes actual")
ma = int(input())
print("Ingrese el dia actual")
da = int(input())

ea = aa - an
em = ma - mn
ed = da - dn 

if(em < 0):
    ea = ea - 1
else:
    if (em == 0)and(ed > 0):
        ea = ea - 1
if (em < 0):
    em = ma + 12 - mn
if (ed < 0):
    ed = da + 30 - dn 

print(f"La edad actual de la persona es: {ea} años con {em} meses y {ed} dias")
    
                