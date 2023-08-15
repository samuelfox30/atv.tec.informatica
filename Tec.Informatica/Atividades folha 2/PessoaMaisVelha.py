nome_pessoa1 = input('Digite o nome da 1º pessoa: ')
idade_pessoa1 = int(input(f'Digite a idade de {nome_pessoa1}: '))

nome_pessoa2 = input('Digite o nome da 2º pessoa: ')
idade_pessoa2 = int(input(f'Digite a idade de {nome_pessoa2}: '))

ano_atual = 2023
ano_nasc_pessoa1 = ano_atual-idade_pessoa1
ano_nasc_pessoa2 = ano_atual-idade_pessoa2

if idade_pessoa1 < idade_pessoa2:
    print(f'{nome_pessoa1} é o mais novo(a), e ele(a) nasceu no ano de {ano_nasc_pessoa1}')

if idade_pessoa1 > idade_pessoa2:
    print(f'{nome_pessoa2} é o mais novo(a), e ele(a) nasceu no ano de {ano_nasc_pessoa2}')
else:
    print(f'{nome_pessoa1} e {nome_pessoa2} tem a mesma idade')