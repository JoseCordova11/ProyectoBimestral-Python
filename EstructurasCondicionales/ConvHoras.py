print("Programa para convertir formata 24 a formato 12 horas")

h24 = 0
m24 = 0
h12 = 0
m12 = 0
periodo = "a.m"

print("Ingrese la hora en formto 24 hora para teransformar")
h24 = int(input())
print("INgrese lo minutos a tranformar")
m24 = int(input())

if h24 < 24 and h24 > 0:
    if(((h24 >= 0) and (h24 <= 24)) and ((m24 >= 0) and (m24 <= 60))) :
        if (m24 == 60):
            h24 = h24 + 1
            m24 = 0
        else:
            m12 = m24
        if (h24 >= 12):
            if (h24 == 12):
                h12 = h24
            else:
                h12 = h24 - 12

                periodo = "p.m"

        print(f"El tiempo de {h24} horas y {m24} minutos ")    
        print(f"Equivale  {h12} horas con {m12} minutos")
else:
    if h24 == 0 :
        h12 = h24
        if m24 == 60 :
            h12 = h12 + 1
            m24 = 0 
        else:
            m12 = m24     
        print(f"El tiempo de {h24} horas y {m24} minutos ")    
        print(f"Equivale  {h12} horas con {m12} minutos")           
    
    else :
        if h24 == 24 :
            h12 = 0
            if m24 == 60 :
                h12 = h12 + 1
                m24 = 0 
            else:
                m12 = m24     
        print(f"El tiempo de {h24} horas y {m24} minutos ")    
        print(f"Equivale  {h12} horas con {m12} minutos")    