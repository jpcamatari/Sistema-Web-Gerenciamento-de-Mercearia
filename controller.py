from model import Categoria, Estoque, Produto, Fornecedor, Cliente, Funcionario, Vendas
from DAO import DaoCategoria, DaoVendas, DaoEstoque, DaoFornecedor, DaoCliente, DaoFuncionario
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True 
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria Cadastrada com Sucesso!')
        else:
            print('A Categoria que deseja cadastrar ja existe')

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) <= 0:
            print('A categoria que deseja remover não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso')
            #TODO: COLOCAR SEM CATEGORIA NO ESTOQUE
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if (x.categoria == categoriaAlterar) else(x), x))
                print('A Alteração foi efetuada com sucesso.')
                #TODO: ALTERAR A CATEGORIA DO ESTOQUE           
            else:
                print('A categoria para qual deseja alterar ja existe')
        else:
            print('A categoria que deseja alterar não existe')
        
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categoria = DaoCategoria.ler()
        if len(categoria) == 0:
            print('Categoria Vazia')
        else:
            for i in categoria:
                print(f'Categorias: {i.categoria}')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produto(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto Cadastrado com sucesso.')
            else:
                print('Produto já existe em Estoque')
        else:
            print('Categoria Inexistente')

    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    print('Produto Removido com Sucesso.')
                    break
        else:
            print('O produto que deseja remover não existe')

        with open('Estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(quantidade))
                arq.writelines('\n')

a = ControllerEstoque()

