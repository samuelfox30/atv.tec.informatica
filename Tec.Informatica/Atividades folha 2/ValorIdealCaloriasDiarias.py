sexo = input('[m] para mulher\n[h] para homem\nVocê é homem ou mulher? ')
peso = float(input('Qual o seu peso? [em kg] '))
altura = float(input('Qual a sua altura? [em cm] '))
idade = int(input('Qual a sua idade? '))

valor_ideal_h = 66+(17.3*peso)+5*altura-6.8*idade
valor_ideal_m = 665+(9.6*peso)+1.8*altura-4.7*idade

if sexo == 'h':
    print(f'O valor ideal para você é {valor_ideal_h}')
else:
    print(f'O valor ideal para você é {valor_ideal_m}')