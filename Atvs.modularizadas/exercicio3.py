from configs import ArquivoDeTexto

nome_do_arquivo_txt = 'estudantes.txt'

while True:
    inf = input('Digite qual informação você quer atualizar: [Nome] [Idade] [Curso]: ')
    inf = inf.lower()
    novo_dado = input('Digite o que você quer escrever no lugar: ')
    
    if ArquivoDeTexto.atualizar_dados(nome_do_arquivo_txt, inf, novo_dado) == True:
        ArquivoDeTexto.imprimir_dados(nome_do_arquivo_txt)
    else:
        pass
    
    repetir = input('Quer atualizar outro dado? [sim] [não]: ')
    repetir = repetir.lower()
    if repetir == 'sim':
        pass
    else:
        break