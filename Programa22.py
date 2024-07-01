import math

def suma():
    print("SUMA")
    num1=int(input("Numero 1:"))
    num2=int(input("Numero 2:"))
    suma=num1+num2
    print(num1,"+",num2,"=",suma)

def resta():
    print("RESTA")
    num1=int(input("Numero 1:"))
    num2=int(input("Numero 2:"))
    resta=num1-num2
    print(num1,"-",num2,"=",resta)

def multiplicacion():
    print("MULRIPLICACIÓN")
    num1=int(input("Numero 1:"))
    num2=int(input("Numero 2:"))
    multiplicacion=num1*num2
    print(num1,"*", num2,"=",multiplicacion)

def division():
    print("DIVISIÓN")
    num1=int(input("Numero 1:"))
    num2=int(input("Numero 2:"))
    division=(num1) / (num2)
    print(num1,"/", num2,"=",division)

print("Selecciona la operacion que deseas realizar")
print("1 - SUMA")
print("2 - RESTA")
print("3 - MULTIPLICACIÓN")
print("4 - DIVISIÓN")

while True:
    opcion = int(input("Opción: "))

    if opcion == 1:
        suma()
    elif opcion == 2:
        resta()
    elif opcion == 3:
        multiplicacion()
    elif opcion == 4:
        division()
    else:
        print("Opción no valida, seleccione otra opcion")
        break

    