while True:
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    suma = num1 + num2
    print("La suma del primer numero y el segundo numero es", suma)
    
    continuar = input("Desea continuar? Sino, ingrese 'n' para detenerse. ")
    if continuar.lower() == 'n':
        break
print("Ha salido del programa.")