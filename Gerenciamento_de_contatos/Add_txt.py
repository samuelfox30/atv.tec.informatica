from configs import Contatos

class Repositoriotxt:

    nome_respositorio = 'contatos.txt'

    def listar():
        contatos = []
        with open(Repositoriotxt.nome_respositorio, 'r') as arquivo:
            dados = arquivo.readlines()
            for dado in dados:
                dado = eval(dado)
                contato = Contatos(dado['Nome'], dado['Endereco'], dado['Telefone'])
                contatos.append(contato)
        return contatos
    
    def adicionar(novo_contato):
        dic_contato = {'Nome': novo_contato.nome, 'Endereco': novo_contato.endereco, 'Telefone': novo_contato.telefone}
        with open(Repositoriotxt.nome_respositorio, 'a') as arquivo:
            arquivo.write(f'{dic_contato}\n')
        print('Novo contato adicionado com sucesso.')

    def alterar(contato_a_alterar):
        nome_referencia = contato_a_alterar.nome_referencia
        tipo_dado = contato_a_alterar.tipo_dado
        novo_dado = contato_a_alterar.novo_dado
        achei = 0
        with open(Repositoriotxt.nome_respositorio, 'r') as arquivo:
            tudo = []
            dados = arquivo.readlines()
            for dado in dados:
                dado = eval(dado)
                tudo.append(dado)
            for t in tudo:
                if tipo_dado == '1':
                    if t['Nome'] == nome_referencia:
                        t['Nome'] = novo_dado
                if tipo_dado == '2':
                    if t['Nome'] == nome_referencia:
                        t['Endereco'] = novo_dado
                if tipo_dado == '3':
                    if t['Nome'] == nome_referencia:
                        t['Telefone'] = novo_dado
        with open(Repositoriotxt.nome_respositorio, 'w') as arquivo:
                arquivo.write('')
        for t in tudo:
            with open(Repositoriotxt.nome_respositorio, 'a') as arquivo:
                arquivo.write(f'{t}\n')

    def excluir(contato_a_deletar):
        nome_referencia = contato_a_deletar.nome_referencia
        achei = 0
        with open(Repositoriotxt.nome_respositorio, 'r') as arquivo:
            tudo = []
            dados = arquivo.readlines()
            for dado in dados:
                dado = eval(dado)
                tudo.append(dado)
            for t in tudo:
                if t['Nome'] == nome_referencia:
                    tudo.remove(t)
        with open(Repositoriotxt.nome_respositorio, 'w') as arquivo:
                arquivo.write('')
        for t in tudo:
            with open(Repositoriotxt.nome_respositorio, 'a') as arquivo:
                arquivo.write(f'{t}\n')

    def pesquisar(contato_a_pesquisar):
        nome_referencia = contato_a_pesquisar.nome_referencia
        achei = 0
        with open(Repositoriotxt.nome_respositorio, 'r') as arquivo:
            tudo = []
            dados = arquivo.readlines()
            for dado in dados:
                dado = eval(dado)
                tudo.append(dado)
            for t in tudo:
                if t['Nome'] == nome_referencia:
                    print(f'O contato encontrado foi: {t}')
                    achei +=1
        if achei == 0:
            print('Nenhum contato foi encontrado!')
            