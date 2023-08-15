numero_inicial = input('Digite o número de 3 digitos: ')
novo_numero = 0

for i in numero_inicial:
    novo_numero = novo_numero + int(i)

verifica1 = novo_numero / 4
verifica2 = 16 / novo_numero
if verifica1.is_integer():
    if verifica2.is_integer():
        print('O número é divisivel por 16 e multiplo de 4')
    else:
        print('O número é multiplo de 4 mas não é divisivel de 16')

else:
    print('O número não é multiplo de 4')