idades = [int(estudante["idade"]) for estudante in estudantes.values()]
idade_media = sum(idades) / len(idades)
print("Idade média dos estudantes:", idade_media)