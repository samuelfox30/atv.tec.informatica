'''
Este é um código que lê N números de numeros inteiros e salva em um arquivo
'''

print('Para parar o loop, digite [sair]')

while True:
    numero = input('Digite um número: ')
    if numero == 'sair':
        break
    else:
        with open('exercicios.txt', 'a') as arquivo:
            arquivo.write(f'{numero}, ')

