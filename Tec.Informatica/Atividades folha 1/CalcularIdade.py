ano_nasc = int(input('Digite seu ano de nascimento: '))
mes_nasc = int(input('Digite seu mes de nascimento: '))
dia_nasc = int(input('Digite seu dia de nascimento: '))

ano_atual = 2023
mes_atual = 8
dia_atual = 7

anos_de_idade = ano_atual - ano_nasc
mes_de_idade = mes_atual - mes_nasc
dia_de_idade = dia_atual - dia_nasc

if mes_de_idade < 0:
    anos_de_idade -= 1

elif mes_de_idade == 0:
    if dia_de_idade < 0:
        anos_de_idade -= 1


print('Você tem ' + str(anos_de_idade) + ' anos de idade')