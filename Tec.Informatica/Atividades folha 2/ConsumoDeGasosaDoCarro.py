km = float(input('Digite quantos km o carro andou: '))
l = float(input('Digite quantos litros o carro usou: '))

consumo = km/l

if consumo<=8:
    print('Venda o carro!')
elif consumo>8 and consumo<14:
    print('Econômico!')
elif consumo>=14:
    print('Super Econômico!')