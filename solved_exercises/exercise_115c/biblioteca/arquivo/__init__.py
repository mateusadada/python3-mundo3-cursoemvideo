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
        for linha in file:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        file.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        file = open(arquivo, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            file.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            file.close()
