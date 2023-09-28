def questao_1():
    dicionario = {}
    dicionario["chave1"] = "valor1"
    dicionario["chave2"] = "valor2"
    dicionario["chave3"] = "valor3"
    print("Dicionário criado com sucesso:", dicionario)


def questao_2():
    dicionario_pessoas = {
        "Alice": 25,
        "Bob": 30,
        "Carol": 22,
        "David": 28
    }
    print("Dicionário de pessoas criado com sucesso:", dicionario_pessoas)


def questao_3(dicionario):
    chaves = list(dicionario.keys())
    print("Chaves:", chaves)


def questao_4(dicionario):
    valores = list(dicionario.values())
    print("Valores:", valores)


def questao_5(dicionario_pessoas, nome):
    idade = dicionario_pessoas.get(nome, "Pessoa não encontrada")
    print(f"A idade de {nome} é {idade} anos.")


def questao_6():
    dicionario_precos = {
        "produto1": 10.0,
        "produto2": 5.0,
        "produto3": 8.0,
        "produto4": 12.0
    }
    lista_compras = ["produto1", "produto3", "produto4"]
    total = sum(dicionario_precos.get(produto, 0) for produto in lista_compras)
    print(f"O valor total da lista de compras é R${total:.2f}")


def questao_7(dicionario_contatos, nome, telefone):
    dicionario_contatos[nome] = telefone
    print(f"Contato {nome} adicionado com sucesso.")


def questao_8(dicionario_contatos, nome):
    if nome in dicionario_contatos:
        del dicionario_contatos[nome]
        print(f"Contato {nome} removido com sucesso.")
    else:
        print(f"Contato {nome} não encontrado.")


def questao_9():
    dicionario_notas = {
        "Aluno1": 8.5,
        "Aluno2": 7.0,
        "Aluno3": 9.5,
        "Aluno4": 6.5
    }
    notas = list(dicionario_notas.values())
    media = sum(notas) / len(notas)
    print(f"A média das notas dos alunos é {media:.2f}")


def questao_10(dicionario_palavras, palavra):
    definicao = dicionario_palavras.get(palavra, "Palavra não encontrada no dicionário.")
    print(f"A definição de '{palavra}' é: {definicao}")


def questao_11(dicionario_paises, pais):
    capital = dicionario_paises.get(pais, "País não encontrado no dicionário.")
    print(f"A capital de '{pais}' é: {capital}")


def questao_12(dicionario_cidades):
    estados = set(dicionario_cidades.values())
    print("Estados sem repetição:", estados)


def questao_13(dicionario_estoques, valor_minimo):
    produtos_baixo_estoque = [produto for produto, estoque in dicionario_estoques.items() if estoque < valor_minimo]
    print("Produtos com estoque abaixo do valor mínimo:", produtos_baixo_estoque)


def questao_14(dicionario_frutas):
    fruta_mais_quantidade = max(dicionario_frutas, key=dicionario_frutas.get)
    quantidade_mais_quantidade = dicionario_frutas[fruta_mais_quantidade]
    print(f"A fruta com maior quantidade é '{fruta_mais_quantidade}' com {quantidade_mais_quantidade} unidades.")


def questao_15(dicionario_alimentos, refeicao):
    total_calorias = sum(dicionario_alimentos.get(alimento, 0) for alimento in refeicao)
    print(f"O total de calorias consumidas na refeição é {total_calorias} calorias.")


def questao_16():
    dicionario_cores = {
        "vermelho": "#FF0000",
        "verde": "#00FF00",
        "azul": "#0000FF",
        "amarelo": "#FFFF00"
    }
    print("Dicionário de cores:", dicionario_cores)


def questao_17(dicionario_filmes):
    filmes_ordenados = sorted(dicionario_filmes.items(), key=lambda x: x[1])
    print("Filmes ordenados por ano de lançamento:")
    for filme, ano in filmes_ordenados:
        print(f"{filme} ({ano})")


def questao_18():
    dicionario_jogadores = {
        "Neymar": [2, 3, 1, 0],
        "Messi": [1, 2, 2, 3],
        "Ronaldo": [3, 2, 1, 1]
    }
    jogador_mais_gols = max(dicionario_jogadores, key=lambda jogador: sum(dicionario_jogadores[jogador]))
    total_gols = sum(dicionario_jogadores[jogador_mais_gols])
    print(f"{jogador_mais_gols} é o jogador com mais gols, com um total de {total_gols} gols.")


def questao_19():
    livro = {
        "Título": "O Pequeno Príncipe",
        "Autor": "Antoine de Saint-Exupéry",
        "Ano": 1943
    }
    print("Informações do livro:")
    for chave, valor in livro.items():
        print(f"{chave}: {valor}")


'''
Professor, essa atividade eu fiz no replit, porque nesse dia meu visual studio tava com uns probleminhas
Então, para facilitar, aqui no final é só você escrever o nome da função que você quer executar
Porque se não eu teria que fazer um if e elif para cada opção, o que iria ficar muito grande

ex:

questao_10()

'''