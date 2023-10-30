from configs import ArquivoDeTexto

""" dicionario = {'Nome': 'Thais', 'Idade': '17', 'Curso': 'Programadora'}
nome_do_arquivo_txt = 'estudantes2.txt'
ArquivoDeTexto.adicionar_a(nome_do_arquivo_txt, dicionario) """

pesquisa = input('Digite qual dado você quer pesuisar: ')
nome_do_arquivo_txt = 'estudantes2.txt'
linha = ArquivoDeTexto.pesquisar_dados(nome_do_arquivo_txt, pesquisa)
confirm = input('Você deseja realmente excluir esta linha? [sim] [não]: ')
if confirm.lower() == 'sim':
    ArquivoDeTexto.deletar_dados(nome_do_arquivo_txt, linha)
elif confirm.lower() == 'nao' or confirm.lower() == 'não':
    print('Ok, repita o processo')
else:
    print('Digita direito po')