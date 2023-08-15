media = float(input('Escreva qual a média do aluno: '))
faltas = float(input(f'Escreva o numero de faltas do aluno: '))

if media < 7:
    if faltas > 32:
        print('Reprovado por média e por faltas')
    else:
        print('Reprovado por média')
else:
    if faltas > 32:
        print('Reprovado por faltas')
    else:
        print('Aprovado')