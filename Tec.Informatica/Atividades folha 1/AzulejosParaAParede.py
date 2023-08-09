'''
Conversor de dolar para real
'''

x_parede = float(input('Digite a largura da parede em cm: '))
y_parede = float(input('Digite a altura da parede em cm: '))

x_azulejo = float(input('Digite a largura do azulejo em cm: '))
y_azulejo = float(input('Digite a altura do azulejo em cm: '))

tamanho_parede = x_parede * y_parede
tamanho_azulejo = x_azulejo * y_azulejo

quantidade_total_em_cm = tamanho_parede / tamanho_azulejo
print('Você precisará de',quantidade_total_em_cm,'cm de azulejo.')
quantidade_aproximada = float(quantidade_total_em_cm / tamanho_azulejo)
print('Isso dá aproximadamente '+ str(int(quantidade_aproximada))+' azulejos.')