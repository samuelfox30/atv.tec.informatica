compras = {}

while True:
    nome_produto = input("Nome do produto (ou 0 para sair): ")
    if nome_produto == "0":
        break
    preco = float(input("Preço do produto: "))
    compras[nome_produto] = preco

valor_total = sum(compras.values())
print(f"Valor total das compras: {valor_total}")

with open("compras.txt", "w") as arquivo:
    arquivo.write(str(compras))