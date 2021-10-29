from typing import cast
import cliente, livros, pagamento, produto, cadastro
from os import system

class Menu:

    def __init__(self):
        self.programa = f'S'
        self.endereco

    def tela(self):
        while (self.programa == 'S'):
            self.endereco = ''
            print(f'Bem vindo(a) à Companhia do Livro!')
            pular_linha()
            cadastro = (f'Por favor, informe se você possui cadastro (S/N)')


def pular_linha():
    print(f'')
        
cliente = Menu()
cliente.set_cadastro