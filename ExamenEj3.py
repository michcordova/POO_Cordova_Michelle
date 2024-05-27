edades = [12,6,26,17,10,58,63,14,18,20,35,63,9]
Infancia = []
Adolecentes = []
Jovenes = []
Adultos = []

print(f"Lista completa: {edades}")

for i in edades:
    if i <= 11: 
        Infancia.append(i)
    elif i <= 17:
        Adolecentes.append(i)
    elif i <= 26:
        Jovenes.append(i)
    else:
        Adultos.append(i)
        
print(f"\Infancia: {Infancia}")
print(f"Adolecentes: {Adolecentes}\n")
print(f"Jovenes: {Jovenes}\n")
print(f"Adultos: {Adultos}\n")