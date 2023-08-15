nome = input('Digite o nome do aluno: ')
nota1 = float(input(f'Digite o valor da primeira nota de {nome}: '))
nota2 = float(input(f'Digite o valor da segunda nota de {nome}: '))

media = (nota1+nota2)/2

if media >= 0 and media < 0:
    print('Reprovado')
elif media >= 5 and media < 7:
    print('Recuperação')
elif media >= 7 and media <= 10:
    print('Aprovado')
else:
    print('O valor está fora dos padrões')