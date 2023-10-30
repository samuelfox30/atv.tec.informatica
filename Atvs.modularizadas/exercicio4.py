from configs import ArquivoDeTexto

""" dicionario = {'Nome': 'Thais', 'Idade': '17', 'Curso': 'Programadora'}
nome_do_arquivo_txt = 'estudantes2.txt'
ArquivoDeTexto.adicionar_a(nome_do_arquivo_txt, dicionario) """

while True:
    pesquisa = input('Digite qual dado você quer pesuisar: ')
    nome_do_arquivo_txt = 'estudantes2.txt'
    if ArquivoDeTexto.pesquisar_dados(nome_do_arquivo_txt, pesquisa) == None:
        print('Nenhum registro encontrado.')

    repetir = input('Quer atualizar outro dado? [sim] [não]: ')
    repetir = repetir.lower()
    if repetir == 'sim':
        pass
    else:
        break