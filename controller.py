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
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')
   
    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))

        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produto(novoNome, novoPreco, novaCategoria), novaQuantidade) if(x.produto.nome == nomeAlterar) else(x), x))
                    print('Produto alterado com sucesso')               
                else:
                    print('Produto ja cadastrado.')
            else:
                print('O produto que deseja alterar não existe.')

            with open('Estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                    arq.writelines('\n')
                
        else:
            print('A categoria informada não existe')

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque Vazio')
        else:
            print('*****Produtos*****')
            for i in estoque:
                print(f"Nome: {i.produto.nome}\n"
                      f"Preco: {i.produto.preco}\n"
                      f"Categoria: {i.produto.categoria}\n"
                      f"Quantidade: {i.quantidade}"

                )
                print("--------------------")

class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)
                        vendido = Vendas(Produto(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)
                        valorCompra = int(quantidadeVendida)*int(i.produto.preco)

                        DaoVendas.salvar(vendido)

            temp.append(Estoque(Produto(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade))              
            arq = open('estoque.txt', 'w')
            arq.write("")

            for i in temp:
                with open('estoque.txt', 'a') as arq:
                    arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                    arq.writelines('\n')

            if existe == False:
                print('O produto não existe')
                return None
            elif not quantidade:
                print('A qauntidade vendida não contem em estoque')
            else:
                return valorCompra


a = ControllerVenda()

a.cadastrarVenda('banana', 'João', 'Caio', 2)

