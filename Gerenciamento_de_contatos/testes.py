import json

meu_dic = {'Nome': 'Samuel', 'Idade': '16', 'Sexo': 'M'}
meu_json = json.dumps(meu_dic)

print(meu_dic)
print(meu_json)
print('\n')
meu_json = json.loads(meu_json)
print(meu_json)
for dado in meu_json.items:
    print(dado)