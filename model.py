from datetime import datetime

class Categoria():
    def __init__(self, categoria):
        self.categoria = categoria

class Produto():
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque():
    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Vendas():
    def __init__(self, produto: Produto, funcionario, cliente, quantidadeVendida, data = datetime.now().strftime("%d/%m/%Y")):

        self.produto = produto
        self.funcionario = funcionario
        self.cliente = cliente
        self.quantidadeVendida = quantidadeVendida
        self.data = data

class Fornecedor():
    def __init__(self, empresa, categoria):
        self.empresa = empresa
        self.categoria = categoria
     
class Cliente():
    def __init__(self, nome_cliente):
        self.nome_cliente = nome_cliente

class Funcionario():
    def __init__(self, nome_fun):
        self.nome_fun = nome_fun


        