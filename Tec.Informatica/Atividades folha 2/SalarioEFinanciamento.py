salario = float(input('Digite seu salário: '))
financiamento = float(input('Digite o valor do financiamento: '))

if financiamento <= salario*5:
    print('Financiamento Concedido')
else:
    print('Financiamento Negado')

print('Obrigado por nos consultar')