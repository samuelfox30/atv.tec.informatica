lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nova_lista = []

for i in lista:
    if i%2 == 0:
        i=0
        nova_lista.append(i)
    else:
        nova_lista.append(i)

print(f'Sua nova lista com todos os numeros pares iguais a 0 fica assim: {nova_lista}')