estudantes = {}

nome = input("Nome do estudante: ")
idade = input("Idade do estudante: ")
curso = input("Curso do estudante: ")

estudantes[nome] = {"idade": idade, "curso": curso}

with open("estudantes.txt", "w") as arquivo:
    arquivo.write(str(estudantes))