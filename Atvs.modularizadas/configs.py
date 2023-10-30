class ArquivoDeTexto:

    def adicionar_w(nome_do_arquivo_txt, dicionario):
        with open(nome_do_arquivo_txt, "w") as arquivo:
            arquivo.write(str(dicionario))

    def adicionar_a(nome_do_arquivo_txt, dicionario):
        with open(nome_do_arquivo_txt, "a") as arquivo:
            arquivo.write('\n' + str(dicionario))

    def imprimir_dados(nome_do_arquivo_txt):
        with open(nome_do_arquivo_txt, "r") as arquivo:
            dados = arquivo.read()
            dados = eval(dados)
            nome = dados['Nome']
            idade = dados['Idade']
            curso = dados['Curso']
            print(f'\nO dicionário está assim: {dados}')
            print('\nMas os dados de forma organizada são esses:')
            print(f'\n{nome} tem {idade} e está cursando {curso}\n')

    def atualizar_dados(nome_do_arquivo_txt, oq_alterar, novo_dado):
        with open(nome_do_arquivo_txt, "r") as arquivo:
            dados = arquivo.read()
            dados = eval(dados)

            if oq_alterar == 'nome':
                dados['Nome'] = novo_dado
            elif oq_alterar == 'idade':
                dados['Idade'] = novo_dado
            elif oq_alterar == 'curso':
                dados['Curso'] = novo_dado
            else:
                print('Digite a informação conforme foi pedido!')
                return False

            with open(nome_do_arquivo_txt, "w") as arquivo:
                arquivo.write(str(dados))
                return True

    def pesquisar_dados(nome_do_arquivo_txt, dado_para_pesquisa):
        with open(nome_do_arquivo_txt, 'r') as arquivo:
            cont = 0
            for linha in arquivo:
                cont+=1
                if dado_para_pesquisa.lower() in linha.lower():
                    print(f'O registro encontrado foi: {linha}')
                    return cont
                    

    def deletar_dados(nome_do_arquivo_txt, num_linha):
        with open(nome_do_arquivo_txt, 'r') as f:
            linhas = f.readlines()

        if num_linha < 1 or num_linha > len(linhas):
            print("Número de linha inválido")
            return

        del linhas[num_linha - 1]

        with open(nome_do_arquivo_txt, 'w') as f:
            f.writelines(linhas)

    
    def media_idades(nome_do_arquivo_txt):
        idades = []
        cont_idades = 0
        resul = 0
        with open(nome_do_arquivo_txt, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                cont_idades += 1
                dado = eval(linha)
                idades.append(dado['Idade'])
            print(idades)
            for idade in idades:
                resul += int(idade)
        return resul/ cont_idades


    def contar_por_curso(nome_do_arquivo_txt):
        cursos = []
        with open(nome_do_arquivo_txt, 'r') as arquivo:

            linhas = arquivo.readlines()
            for linha in linhas:
                dado = eval(linha)
                curso = dado['Curso']
                print(curso)
                cursos.append(curso)

            curso_set = set(cursos)
            qt_cursos_existem = len(curso_set)

            contagem_por_id = []
            for curso in curso_set:
                contagem_por_id.append(0)

            for curso in cursos:
                id_curso = 0
                for setp in curso_set:
                    id_curso += 1
                    if curso == setp:
                        contagem_por_id[id_curso-1] += id_curso

            print(f'Existem {qt_cursos_existem} diferentes, que são {curso_set}')
            pos = 0
            for curso in curso_set:
                print(f'O curso de {curso} existem {int(contagem_por_id[pos]/(pos+1))} pessoas matriculadas.')
                pos += 1


class Contatos:

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def salvar(self):
        dicionario = {'Nome':self.nome,'Telefone':self.telefone}
        with open('lista_de_contatos.txt', 'a') as arquivo:
            arquivo.write(f'{str(dicionario)}\n')

    def show():
        with open('lista_de_contatos.txt', 'r') as arquivo:
            contatos = arquivo.read()
            print(contatos)

    def search(tipo, dado):
        with open('lista_de_contatos.txt', 'r') as arquivo:
            contatos = arquivo.readlines()
            achou = 0
            num_linha = 0
            for contato in contatos:
                num_linha += 1
                dicionario_contato = eval(contato)
                if tipo == 'Nome':
                    if dado == dicionario_contato['Nome']:
                        print(f'O registro >{dado}< Existe nessa linha: {dicionario_contato}')
                        achou += 1
                elif tipo == 'Telefone':
                    if dado == dicionario_contato['Telefone']:
                        print(f'O registro >{dado}< Existe nessa linha: {dicionario_contato}')
                        achou += 1
            if achou == 0:
                print(f'Registro {dado} não encontrado')
