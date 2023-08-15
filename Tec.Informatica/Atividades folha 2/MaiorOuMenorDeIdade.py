sexo = input('Você é homem ou mulher? [h ou m] ')
idade = int(input('Quantos anos você tem? '))

if sexo == 'h':
    if idade >=21 :
        print('Você é maior de idade!')
    else:
        print('Você é menor de idade!')
else:
    if idade >=18 :
        print('Você é maior de idade!')
    else:
        print('Você é menor de idade!')