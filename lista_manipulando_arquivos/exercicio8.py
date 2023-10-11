agenda_contatos = {}

def adicionar_contato():
    nome = input("Nome do contato: ")
    telefone = input("Número de telefone: ")
    agenda_contatos[nome] = telefone

def visualizar_contatos():
    for nome, telefone in agenda_contatos.items():
        print(f"Nome: {nome}, Telefone: {telefone}")

def atualizar_contato():
    nome = input("Nome do contato a ser atualizado: ")
    if nome in agenda_contatos:
        novo_telefone = input("Novo número de telefone: ")
        agenda_contatos[nome] = novo_telefone

def excluir_contato():
    nome = input("Nome do contato a ser excluído: ")
    if nome in agenda_contatos:
        del agenda_contatos[nome]