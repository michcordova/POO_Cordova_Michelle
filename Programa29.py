def encapsulamiento():
    print("Consiste en hacer que los atributos o métodos internos a una clase no se puedan acceder ni modificar desde fuera, sino que tan solo el propio objeto pueda acceder a ellos.")
    return

def abstraccion():
    print("Consiste en ocultar toda la complejidad que algo puede tener por dentro")
    return

def herencia():
    print("Proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, compartiendo sus métodos y atributos.")
    return

def polimorfismo():
    print("Es la capacidad de objetos de diferentes clases para responder al mismo mensaje")
    return

def opcion():
    while True:
        print("Seleccione la opción de la cual desea ver su significado")
        print("--------------------------------------------------------")
        print("MENU")
        print("--------------------------------------------------------")
        print("1. Encapsulamiento")
        print("2. Abstracción")
        print("3. Herencia")
        print("4. Polimorfismo")
        print("5. Salir")

        opcion = int(input("Ingrese su opción: "))
        print("--------------------------------------------------------")

        if opcion == 1:
            encapsulamiento()
        elif opcion == 2:
            abstraccion()
        elif opcion == 3:
            herencia()
        elif opcion == 4:
            polimorfismo()
        elif opcion == 5:
            print("Ha salido del programa.")
            break
        else:
            print("Opción no válida.")

opcion()
