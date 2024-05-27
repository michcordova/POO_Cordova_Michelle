while True:
    print("Ingrese el numero del área que desea calcular:")
    print("1. Área de un cuadrado")
    print("2. Área de un triángulo")
    print("3. Área de un rectángulo")
    print("4. Salir")

    opcion = int(input("Ingresa el número de la opción deseada: "))
    if opcion == 1:
        lado = float(input("Ingresa la medida de un lado del cuadrado: "))
        area_cuadrado = lado * lado
        print("El área del rectángulo es:", area_cuadrado, "cm2")

    elif opcion == 2:
        base = float(input("Ingresa la longitud de la base del triangulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area_triangulo = base * altura / 2
        print("El área del triangulo es:", area_triangulo, "cm2")
    elif opcion == 3:
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        area_rectangulo = base * altura
        print("El area del rectángulo es:", area_rectangulo, "cm2")
    elif opcion == 4:
        print("Ha salido del programa")
        break
    else:
        print("Opción no válida..")
