print('Informe o valor dos 3 ângulos do triângulo')
a1 = int(input('1º ângulo: '))
a2 = int(input('2º ângulo: '))
a3 = int(input('3º ângulo: '))

if a1 < 90 and a2 < 90 and a3 < 90:
    print('Este é um triângulo acutângulo!')
elif a1 == 90 or a2 == 90 or a3 == 90:
    print('Este é um triângulo retângulo!')
elif a1 > 90 or a2 > 90 or a3 > 90:
    print('Este é um triângulo obtusângulo!')
else:
    print('Os ângulos informados não formam um triângulo')