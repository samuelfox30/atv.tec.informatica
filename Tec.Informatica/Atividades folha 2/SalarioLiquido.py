salario_bruto = float(input('Digite o salário bruto: '))

if salario_bruto <= 1903.98:
  print(f'Seu salário será de {salario_bruto}')

elif salario_bruto > 1903.98 and salario_bruto <= 2826.65:
  imposto = 0.075
  deducao = 142.80
  desconto = salario_bruto * imposto - deducao
  print(desconto)
  print(f'Seu salário será de {salario_bruto-desconto}')

elif salario_bruto > 2826.65 and salario_bruto <= 3751.05:
  imposto = 0.15
  deducao = 548.82
  desconto = salario_bruto * imposto - deducao
  print(desconto)
  print(f'Seu salário será de {salario_bruto-desconto}')

elif salario_bruto > 3751.05 and salario_bruto <= 4664.68:
  imposto = 0.225
  deducao = 636.13
  desconto = salario_bruto * imposto - deducao
  print(desconto)
  print(f'Seu salário será de {salario_bruto-desconto}')

elif salario_bruto > 4664.68:
  imposto = 0.275
  deducao = 869.36
  desconto = salario_bruto * imposto - deducao
  print(desconto)
  print(f'Seu salário será de {salario_bruto-desconto}')