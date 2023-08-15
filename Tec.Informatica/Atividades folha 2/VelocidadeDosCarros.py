distancia_carro1 = float(input('Digite a distância percorrida pelo 1º carro: '))
tempo_carro1 = float(input('Digite o tempo que o 1º carro levou no percurso [em horas]: '))

distancia_carro2 = float(input('Digite a distância percorrida pelo 2º carro: '))
tempo_carro2 = float(input('Digite o tempo que o 2º carro levou no percurso [em horas]: '))

velocidade_media_carro1 = distancia_carro1/tempo_carro1
velocidade_media_carro2 = distancia_carro2/tempo_carro2

if velocidade_media_carro1 > velocidade_media_carro2:
    print('O carro 1 estava mais rápido')
elif velocidade_media_carro1 < velocidade_media_carro2:
    print('O carro 2 estava mais rápido')
else:
    print('As velocidades são iguais')