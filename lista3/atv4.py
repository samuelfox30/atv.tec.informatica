print('Para parar de adicionar palavras na lista digite a palavra [parar]')
lista_do_usuario = []

while True:
    item = input('Digite o item: ')
    if item == 'parar':
        break
    else:
        lista_do_usuario.append(item)


print(f'Sua lista: {lista_do_usuario}')