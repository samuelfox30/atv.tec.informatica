with open("estudantes.txt", "r") as arquivo:
    estudantes = eval(arquivo.read())

for nome, info in estudantes.items():
    print("Nome:", nome)
    print("Idade:", info["idade"])
    print("Curso:", info["curso"])