aco = float(input('Quantas hastes de aço você comprou? '))
cobre = float(input('Quantas hastes de cobre você comprou? '))
aluminio = float(input('Quantas hastes de alumínio você comprou? '))

preco_sem_desconto = aco*2.50 + cobre*4 + aluminio*5
quantidade_de_hastes = aco+cobre+aluminio

if quantidade_de_hastes < 6:
    print(f'O valor a ser pago será de {preco_sem_desconto}')

elif quantidade_de_hastes > 6 and quantidade_de_hastes < 15:
    print(f'O valor a ser pago será de {preco_sem_desconto-(0.1*preco_sem_desconto)}')

elif quantidade_de_hastes > 15 and quantidade_de_hastes < 20:
    print(f'O valor a ser pago será de {preco_sem_desconto-(0.15*preco_sem_desconto)}')

elif quantidade_de_hastes > 20:
    print(f'O valor a ser pago será de {preco_sem_desconto-(0.2*preco_sem_desconto)}')