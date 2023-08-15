tipo_de_consumidor = input('Qual o tipo de consumidor?\n[I] Industrial\n[C] Comercial\n[R] Residêncial\n-: ')
consumo = float(input('Digite qual foi o valor do consumo: '))

if tipo_de_consumidor == 'I':
    print(f'Você deverá pagar: {0.68*consumo+34}')

elif tipo_de_consumidor == 'C':
    print(f'Você deverá pagar: {0.37*consumo+45}')

elif tipo_de_consumidor == 'C':
    print(f'Você deverá pagar: {0.77*consumo-22}')