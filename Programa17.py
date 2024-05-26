while True:
    print("Menu")
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Fahrenheit a Celsius")
    print("3. Salir")
    
    opcion = int(input("Elija una opción: "))
    
    if opcion == 1:
        celsius = float(input("Ingresa la temperatura en grados Celsius: "))
        fahrenheit = 9.0/5.0 * celsius + 32
        print("La temperatura en grados Fahrenheit es: ", fahrenheit)
    elif opcion == 2:
        fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5.0/9.0
        print("La temperatura en grados Celsius es: ", celsius)
    elif opcion == 3:
        print("Ha salido del programa.")
        break
    else:
        print("Opción no válida.")
