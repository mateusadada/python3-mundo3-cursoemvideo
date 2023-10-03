def arquivo_existe(nome):
    try:
        file = open(nome, 'rt')
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        file = open(nome, 'wt+')
        file.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo \033[33m{nome}\033[m criado com sucesso!')


def ler_arquivo(nome):
    try:
        file = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print('-' * 42)
        print('PESSOAS CADASTRADAS'.center(42))
        print('-' * 42)
        print(file.read())
