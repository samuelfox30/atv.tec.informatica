print('Para parar de adicionar palavras na lista digite a palavra [parar]')
lista_do_usuario = []
lista_final = []

while True:
    palavra = input('Digite a palavra: ')
    if palavra == 'parar':
        break
    else:
        lista_do_usuario.append(palavra)

for i in lista_do_usuario:
    verificar = len(i)
    if verificar < 6:
        lista_final.append(i)


print(f'Você digitou as palavras: {lista_do_usuario}')
print(f'E as palavras que tem apenas 5 letras são: {lista_final}')