contagem_cursos = {}

for estudante in estudantes.values():
    curso = estudante["curso"]
    if curso in contagem_cursos:
        contagem_cursos[curso] += 1
    else:
        contagem_cursos[curso] = 1

for curso, count in contagem_cursos.items():
    print(f"{curso}: {count} estudantes")