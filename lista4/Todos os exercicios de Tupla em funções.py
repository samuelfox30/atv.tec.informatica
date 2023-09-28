def atv_tupla_1():
  tupla_numeros = (1, 2, 3, 4, 5)
  print(tupla_numeros)

def atv_tupla_2():
  tupla_vazia = ()
  tupla_vazia += (1, 2, 3, 4, 5)
  print(tupla_vazia)

def atv_tupla_3():
  cores = ("vermelho", "verde", "azul", "amarelo", "roxo")
  cores_ordenadas = tuple(sorted(cores))
  print(cores_ordenadas)

def atv_tupla_4():
  tupla_numeros = (1, 2, 3, 4, 5)
  soma = 0
  for numero in tupla_numeros:
      soma += numero
  print("A soma dos elementos da tupla é:", soma)

def atv_tupla_5():
  tupla_numeros = (10, 5, 23, 8, 14, 2)
  maior_valor = max(tupla_numeros)
  menor_valor = min(tupla_numeros)
  print("O maior valor na tupla é:", maior_valor)
  print("O menor valor na tupla é:", menor_valor)

def atv_tupla_6():
  tupla1 = (1, 2, 3)
  tupla2 = (4, 5, 6)
  tupla3 = tupla1 + tupla2
  print(tupla3)

def atv_tupla_7():
  tupla_strings = ("Python", "Programação", "Tupla", "Texto", "Linguagem")
  contagem = 0
  for palavra in tupla_strings:
      if len(palavra) > 5:
          contagem += 1
  print("O número de strings com mais de 5 caracteres é:", contagem)

def atv_tupla_8():
  tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
  numero_verificado = 5
  if numero_verificado in tupla_numeros:
      print(f"O número {numero_verificado} está presente na tupla.")
  else:
      print(f"O número {numero_verificado} não está presente na tupla.")

def atv_tupla_9():
  tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
  tupla_pares = tuple(x for x in tupla_numeros if x % 2 == 0)
  print(tupla_pares)

def atv_tupla_10():
  tupla_palavras = ("Python", "Programação", "Tupla", "Texto", "Linguagem")
  tupla_comprimentos = tuple(len(palavra) for palavra in tupla_palavras)
  print(tupla_comprimentos)

def atv_tupla_11():
  tupla_numeros = (10, 15, 20, 25, 30)
  soma = sum(tupla_numeros)
  num_elementos = len(tupla_numeros)
  media = soma / num_elementos
  print("A média dos valores na tupla é:", media)

def atv_tupla_12():
  tupla_datas = (
      (5, 10, 2020),
      (12, 4, 2019),
      (8, 7, 2022),
      (1, 1, 2021),
  )
  tupla_datas_ordenadas = tuple(sorted(tupla_datas, key=lambda data: (data[2], data[1], data[0])))
  for data in tupla_datas_ordenadas:
      print(f"{data[0]}/{data[1]}/{data[2]}")

def atv_tupla_13():
  tupla_numeros = (2, 4, 6, 8, 10)
  todos_pares = True
  for numero in tupla_numeros:
      if numero % 2 != 0:
          todos_pares = False
          break
  if todos_pares:
      print("Todos os elementos da tupla são pares.")
  else:
      print("Pelo menos um elemento da tupla não é par.")

def atv_tupla_14():
  tupla_original = (1, 2, 2, 3, 4, 4, 5, 5)
  conjunto_sem_repeticao = set(tupla_original)
  nova_tupla = tuple(conjunto_sem_repeticao)
  print(nova_tupla)

def atv_tupla_15():
  tupla_frutas = ("maçã", "banana", "laranja", "uva", "manga", "abacaxi")
  fruta_especifica = "uva"
  if fruta_especifica in tupla_frutas:
      posicao = tupla_frutas.index(fruta_especifica) + 1  
      print(f"A fruta '{fruta_especifica}' está na posição {posicao} da tupla.")
  else:
      print(f"A fruta '{fruta_especifica}' não foi encontrada na tupla.")

def atv_tupla_16():
  tupla1 = (1, 2, 3, 4, 5)
  tupla2 = (6, 7, 8, 9, 10)
  tupla_soma = tuple(x + y for x, y in zip(tupla1, tupla2))
  print(tupla_soma)

def atv_tupla_17():
  tupla_paises_populacao = (
      ("China", 1444216107),
      ("Índia", 1380004385),
      ("Estados Unidos", 331002651),
      ("Indonésia", 273523615),
      ("Paquistão", 220892340)
  )
  
  pais_mais_populoso = ""
  populacao_mais_populosa = 0
  
  for pais, populacao in tupla_paises_populacao:
      if populacao > populacao_mais_populosa:
          pais_mais_populoso = pais
          populacao_mais_populosa = populacao

  print(f"O país mais populoso é {pais_mais_populoso} com uma população de {populacao_mais_populosa} pessoas.")

def atv_tupla_18():
  tupla_notas = (7.5, 9.0, 6.2, 8.5, 6.8, 8.0, 9.5) 
  tupla_notas_crescente = tuple(sorted(tupla_notas))
  print(tupla_notas_crescente)

def atv_tupla_19():
  tupla_numeros = (15, 20, 8, 12, 18)
  todos_maiores_que_10 = True
  for numero in tupla_numeros:
      if numero <= 10:
          todos_maiores_que_10 = False
          break  
  if todos_maiores_que_10:
      print("Todos os elementos da tupla são maiores que 10.")
  else:
      print("Pelo menos um elemento da tupla não é maior que 10.")

def atv_tupla_20():
  tupla_animais = ("gato", "cachorro", "peixe", "elefante", "pássaro", "cobra")
  tupla_animais_ordenados = tuple(sorted(tupla_animais))
  tres_primeiros_alfabeticamente = tupla_animais_ordenados[:3]
  print("Os três primeiros animais em ordem alfabética são:", tres_primeiros_alfabeticamente)


'''
Professor, essa atividade eu fiz no replit, porque nesse dia meu visual studio tava com uns probleminhas
Então, para facilitar, aqui no final é só você escrever o nome da função que você quer executar
Porque se não eu teria que fazer um if e elif para cada opção, o que iria ficar muito grande

ex:

atv_tupla_10()

'''