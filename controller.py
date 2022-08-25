from DAO import DaoCategoria, DaoVendas
from model import *


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
            else:
                print('A categoria para qual deseja alterar ja existe')
        else:
            print('A categoria que deseja alterar não existe')
        
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')
