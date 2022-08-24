from turtle import st
from model import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open("Categoria.txt", 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open("Categoria.txt", 'r') as arq:
            cls.categoria = arq.readlines()
        
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
       
        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))

        return cat

class DaoVendas:
    @classmethod
    def salvar(cls, vendas: Vendas):
        with open("Vendas.txt", 'a') as arq:
            arq.writelines(vendas.produto.nome + "|" + vendas.produto.preco + "|" + vendas.produto.categoria + "|" + vendas.funcionario + "|" + 
            vendas.cliente + "|" + str(vendas.quantidadeVendida) + "|" + vendas.data)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open("Vendas.txt", 'r') as arq:
            cls.vendas = arq.readlines()
        
        cls.vendas = list(map(lambda x: x.replace('\n', ''), cls.vendas))
        cls.vendas = list(map(lambda x: x.split('|'), cls.vendas))
        ven = []
        for i in cls.vendas:
            ven.append(Vendas(Produto(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return ven

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produto, quantidade):
        with open("Estoque.txt", 'a') as arq:
            arq.writelines(produto.nome + '|' + produto.preco + '|' + produto.categoria + '|' + str(quantidade))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open("Estoque.txt", 'r') as arq:
            cls.estoque = arq.readlines()
        
        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produto(i[0], i[1], i[2]), int(i[3])))

        return est

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open("Fornecedor.txt", 'a') as arq:
            arq.writelines(fornecedor.empresa + '|' + fornecedor.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open("Fornecedor.txt", 'r') as arq:
            cls.fornecedor = arq.readlines()

        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))
        forn = []
        for i in cls.fornecedor:
            forn.append(Fornecedor(i[0], i[1]))

        return forn

class DaoCliente:
    @classmethod
    def salvar(cls, cliente: Cliente):
        with open("Cliente.txt", 'a') as arq:
            arq.writelines(cliente.nome_cliente)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open("Cliente.txt", 'r') as arq:
            cls.cliente = arq.readlines()
        
        cls.cliente = list(map(lambda x: x.replace('\n', ''), cls.cliente))
        cli = []
        for i in cls.cliente:
            cli.append(Cliente(i))

        return cli


class DaoProduto:
    @classmethod
    def salvar(cls, produto: Produto):
        with open("Produto.txt", 'a') as arq:
            arq.writelines(produto.nome)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open("Produto.txt", 'r') as arq:
            cls.produto = arq.readlines()
        
        cls.produto = list(map(lambda x: x.replace('\n', ''), cls.produto))
        pro = []
        for i in cls.produto:
            pro.append(Produto(i))

        return pro

class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open("Funcionario.txt", 'a') as arq:
            arq.writelines(funcionario.nome_fun)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open("Funcionario.txt", 'r') as arq:
            cls.funcionario = arq.readlines()
        
        cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))
        fun = []
        for i in cls.funcionario:
            fun.append(Funcionario(i))

        return fun