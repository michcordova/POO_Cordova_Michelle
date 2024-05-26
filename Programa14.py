edades = [12,5,20,17,10,58,63,14,18,20,35,63,9]
may_edad = []
men_edad = []

print(f"\nLista completa: {edades}")

for i in edades:
    if i <= 17: 
        men_edad.append(i)
    else:
        may_edad.append(i)
        
print(f"\nMenores de edad: {men_edad}")
print(f"Adultos:  {may_edad}\n")