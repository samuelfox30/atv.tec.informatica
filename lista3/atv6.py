lista = [2,3,4,5,3,65,3,6,6,8,8,5,3,6,5]
nova_lista = []

for i in lista:
    if i in nova_lista:
        pass
    else:
        nova_lista.append(i)

print(f'Sua lista sem números repetidos é: {nova_lista}')