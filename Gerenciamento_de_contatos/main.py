from configs import *
from Add_txt import Repositoriotxt


def listar():
    contatos = Repositoriotxt.listar()
    for contato in contatos:
        print(f'\n{contato}')
    
def criar():
    nome = input('Digite o nome do novo contato: ')
    endereco = input('Digite o endereço do novo contato: ')
    telefone = input('Digite o telefone do novo contato: ')
    novo_contato = Contatos(nome, endereco, telefone)
    Repositoriotxt.adicionar(novo_contato)

def editar():
    while True:
        nome_referencia = input('Favor digite o nome do contato que deseja editar: ')
        print('Digite qual dado você deseja alterar:\n[1] Nome\n[2] Endereco\n[3] Telefone')
        tipo_dado = input('=: ')
        novo_dado = input('Digite o novo dado: ')
        if tipo_dado == '1' or tipo_dado == '2' or tipo_dado == '3':
            contato_a_alterar = Alterar(nome_referencia, tipo_dado, novo_dado)
            Repositoriotxt.alterar(contato_a_alterar)
            break
        else:
            print('Não entendi sua resposta, favor digite apenas um dos números oferecidos.')

def deletar():
    nome_referencia = input('Favor digite o nome do contato que deseja excluir: ')
    contato_a_alterar = Excluir(nome_referencia)
    Repositoriotxt.excluir(contato_a_alterar)

def pesquisar():
    nome_referencia = input('Favor digite o nome do contato que deseja pesquisar: ')
    contato_a_pesquisar = Pesquisar(nome_referencia)
    Repositoriotxt.pesquisar(contato_a_pesquisar)


print('''
-----------------------------------------------------------
------ESTE É UM PROGRAMA DE GERENCIAMENTO DE CONTATOS------
-----------------------------------------------------------
''')

while True:

    print('\n--------------------------------------------------------')
    print('Escolha qual ação você deseja tomar (digite o número):')
    print('[1] Listar contato\n[2] Criar contatos\n[3] Editar contatos\n[4] Deletar contatos\n[5] Pesquisar contatos')
    acao = input('=: ')

    if acao == '1':
        listar()

    elif acao == '2':
        criar()

    elif acao == '3':
        editar()

    elif acao == '4':
        deletar()

    elif acao == '5':
        pesquisar()

    else:
        print('Não entendi sua resposta, porfavor digite apenas os números oferecidos.')
