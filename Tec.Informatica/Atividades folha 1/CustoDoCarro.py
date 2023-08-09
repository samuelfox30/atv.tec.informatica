custo_de_fabrica = float(input('Digite o custo de fabrica o carro: R$'))

imposto_aplicado = (0.01*custo_de_fabrica)*45
percentual_vendedor = (0.01*custo_de_fabrica)*28
preco_final = custo_de_fabrica+imposto_aplicado+percentual_vendedor

print('O preço final é R$'+str(preco_final))