
edades = [15, 22, 17, 19, 35, 12, 45, 67]

adultos = []
menores = []

for edad in edades:
    if edad >= 18:
        adultos.append(edad)
    else:
        menores.append(edad)

print("Lista de adultos:", adultos)
print("Lista de menores:", menores)
