# Crear tres conjuntos
conjunto1 = {1, 3, 5, 7, 9}
conjunto2 = {2, 4, 6, 8, 10}
conjunto3 = {11, 13, 15, 17, 19}
union = conjunto1 | conjunto2 | conjunto3
print("Union de los 3 conjuntos:", union)

conjunto_pares = {valor for valor in union if valor % 2 == 0}
print("Conjunto de valores pares:", conjunto_pares)