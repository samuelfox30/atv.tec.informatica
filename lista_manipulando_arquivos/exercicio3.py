nome = input("Nome do estudante a ser atualizado: ")
if nome in estudantes:
    idade = input("Nova idade: ")
    curso = input("Novo curso: ")
    estudantes[nome]["idade"] = idade
    estudantes[nome]["curso"] = curso

    with open("estudantes.txt", "w") as arquivo:
        arquivo.write(str(estudantes))