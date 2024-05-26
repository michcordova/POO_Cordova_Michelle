promedio1 = float(input("Ingresa el primer promedio: "))
promedio2 = float(input("Ingresa el segundo promedio: "))
promedio3 = float(input("Ingresa el tercer promedio: "))

if promedio1 >= promedio2 and promedio1 >= promedio3:
    print("El primer promedio es el mayor.")
elif promedio2 >= promedio1 and promedio2 >= promedio3:
    print("El segundo promedio es el mayor.")
else:
    print("El tercer promedio es el mayor.")