# help(function) - Mostra a documentação (docstrings) da função/método.
# Docstrings começo na linha abaixo do início da função com separação de três aspas duplas.

def counter(start, stop, step):
    """
    Faz uma contagem de números inteiros e mostra na tela.\n
    Função criada por Mateus Adada.
    :param start: Início da contagem
    :param stop: Fim da contagem
    :param step: Passo da contagem
    :return: Sem retorno
    """
    for value in range(start, stop + 1, step):
        print(value, end=' ')
    print('FIM!')


# counter(2, 10, 2)
help(counter)
