# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto
# simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from menu import menu, cabecalho
from time import sleep
from arquivo import *

print('Bem-vindo ao programa que exibe um MENU interativo!')

arquivo = 'base_de_dados.txt'

if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if resposta == 1:
        # listar o conteúdo da base de dados
        ler_arquivo(arquivo)

    elif resposta == 2:
        cabecalho('Opção 2')

    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break

    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')

    sleep(1)
