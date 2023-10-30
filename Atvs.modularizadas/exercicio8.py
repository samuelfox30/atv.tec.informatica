from configs import ArquivoDeTexto

inf = input('Digite qual informação você quer atualizar: [Nome] [Numero]: ')
nome_do_arquivo_txt = 'lista_de_contatos.txt'
novo_dado = input('Digite o que você quer escrever no lugar: ')

ArquivoDeTexto.atualizar_dados(nome_do_arquivo_txt, inf, novo_dado)