import csv

# Dicionário de compras do Exercício 9
compras = {
    "Produto 1": 10.0,
    "Produto 2": 20.0,
    "Produto 3": 30.0,
    "Produto 4": 40.0,
}

# Nome do arquivo CSV de saída
nome_arquivo = "compras.csv"

# Abrir o arquivo CSV para escrita
with open(nome_arquivo, 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    # Escrever o cabeçalho (opcional)
    escritor_csv.writerow(["Nome do Produto", "Preço"])

    # Escrever os dados do dicionário no arquivo CSV
    for produto, preco in compras.items():
        escritor_csv.writerow([produto, preco])

print(f'Dados exportados para {nome_arquivo}')