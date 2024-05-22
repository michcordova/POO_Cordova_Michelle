peso = int(input("Ingrese el peso de su paquete:" ))
if peso < 1:
    costo = 50
elif peso < 5:
    costo = 100
elif peso < 10:
    costo = 200
else:
    costo = 500

print("El costo de envío es: $", costo)