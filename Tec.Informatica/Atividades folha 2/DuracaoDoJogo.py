print('O jogo só pode ter no máximo 24 horas de duração!')

hora_iniciou = int(input('Digite o hora inicial do jogo: '))
minuto_iniciou = int(input('Digite o minuto inicial do jogo: '))

hora_terminou = int(input('Digite o hora final do jogo: '))
minuto_terminou = int(input('Digite o minuto final do jogo: '))

hora_duracao = abs(hora_iniciou - hora_terminou)
minuto_duracao = abs(minuto_iniciou - minuto_terminou)

print(hora_duracao)
print(minuto_duracao)