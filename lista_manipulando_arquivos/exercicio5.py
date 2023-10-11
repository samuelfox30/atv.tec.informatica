nome = input("Nome do estudante a ser removido: ")
if nome in estudantes:
    del estudantes[nome]

    with open("estudantes.txt", "w") as arquivo:
        arquivo.write(str(estudantes))