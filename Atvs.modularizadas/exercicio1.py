from configs import ArquivoDeTexto


nome = input('Digite o nome do aluno(a): ')
idade = input('Digite a idade do aluno(a): ')
curso = input('Digite o curso do aluno(a): ')

dicionario = {'Nome': nome, 'Idade': idade, 'Curso': curso}

nome_do_arquivo_txt = 'estudantes.txt'
ArquivoDeTexto.adicionar_w(nome_do_arquivo_txt, dicionario)