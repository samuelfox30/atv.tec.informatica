nome = input("Nome do estudante a ser pesquisado: ")
if nome in estudantes:
    info = estudantes[nome]
    print("Nome:", nome)
    print("Idade:", info["idade"])
    print("Curso:", info["curso"])
else:
    print("Estudante não encontrado.")