print("Programa para calcular el valor total de una factura con descuentos")

subtotal = 0 
total = 0
descuento = 0
limite1 = 200
limite2 = 500

print("Ingrese el subtotal de la compra")
subtotal = float(input())

if subtotal >= limite1 and subtotal < limite2 :
    descuento = 0.10
else:
    if subtotal >= limite2 :
        descuento = 0.15

if subtotal < limite1:
    print("No hay un descuento por su compra por ser menor a 200 dolares")

total = subtotal - (subtotal * descuento)

print(f"El total de la factura es {total} con un descuento de {descuento}")
