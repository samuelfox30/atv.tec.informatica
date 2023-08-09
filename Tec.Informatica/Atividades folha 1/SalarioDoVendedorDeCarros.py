salario_fixo = float(input('Digite seu salario fixo: R$'))
quantidade_de_carros = float(input('Quantos carros você vendeu este mês? '))
preco_total_vendido = float(input('Qual foi o valor total de suas vendas? '))
comissao_por_carro = float(input('Qual o valor da sua comissão? [digite a porcentagem sem o %] '))

valor_individual_carro = preco_total_vendido/quantidade_de_carros

comissao = (0.01*valor_individual_carro)*quantidade_de_carros
taxa_do_valor_total = (0.01*preco_total_vendido)*5

resultado_final = salario_fixo+comissao+taxa_do_valor_total

print('Seu salário será de R$'+str(resultado_final))