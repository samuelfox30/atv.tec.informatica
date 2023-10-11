import csv

with open("compras.csv", "w", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    for nome_produto, preco in compras.items():
        escritor.writerow([nome_produto, preco])