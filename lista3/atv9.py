lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [55, 3, 4, 7, 443, 66, 645]
numeros_repetidos = []

for i in lista1:
    if i in lista2:
        numeros_repetidos.append(i)

print(f'Os números que se repetem são: {numeros_repetidos}')