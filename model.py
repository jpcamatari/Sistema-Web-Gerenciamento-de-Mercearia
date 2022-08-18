from datetime import datetime

class Categoria():
    def __init__(self, categoria):
        self.categoria = categoria

class Fornecedor():
    def __init__(self, empresa, categoria):
        self.empresa = empresa
        self.categoria = categoria


class Produto():
    def __init__(self, nome_produto, categoria, fornecedor, preco):
        self.nome_produto = nome_produto
        self.categoria = categoria
        self.fornecedor = fornecedor
        self.preco = preco


class Estoque():
    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Cliente():
    def __init__(self, nome_cliente):
        self.nome_cliente = nome_cliente

class Funcionario():
    def __init__(self, nome_fun):
        self.nome_fun = nome_fun

class Vendas():
    def __init__(self, funcionario, cliente, produto: Produto, quantidade, data = datetime.now().strftime("%d/%m/%Y")):

        self.funcionario = funcionario
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.data = data
        