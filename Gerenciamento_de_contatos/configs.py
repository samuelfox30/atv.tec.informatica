class Contatos:

    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}\nEndereco: {self.endereco}\nTelefone: {self.telefone}"


class Alterar:

    def __init__(self, nome_referencia, tipo_dado, novo_dado):
        self.nome_referencia = nome_referencia
        self.tipo_dado = tipo_dado
        self.novo_dado = novo_dado

    def __str__(self):
        return f'Nome: {self.nome_referencia}, Tipo do dado: {self.tipo_dado}, Novo dado: {self.novo_dado}'
    

class Excluir:

    def __init__(self, nome_referencia):
        self.nome_referencia = nome_referencia

    def __str__(self):
        return f'Nome: {self.nome_referencia}'
    

class Pesquisar:

    def __init__(self, nome_referencia):
        self.nome_referencia = nome_referencia

    def __str__(self):
        return f'Nome: {self.nome_referencia}'