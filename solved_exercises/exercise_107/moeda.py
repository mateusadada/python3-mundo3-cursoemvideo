# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça
# também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(price, percentage):
    """
    Aumenta um preço com base em uma porcentagem passada.
    :param price: O preço.
    :param percentage: A porcentagem.
    :return: O preço.
    """
    res = price * (1 + percentage / 100)
    return res


def diminuir(price, percentage):
    """
    Diminui um preço com base em uma porcentagem passada.
    :param price: O preço.
    :param percentage: A porcentagem.
    :return: O preço.
    """
    res = price * (1 - percentage / 100)
    return res


def dobro(price):
    """
    Faz o cálculo do dobro de um preço.
    :param price: O preço.
    :return: O preço.
    """
    res = price * 2
    return res


def metade(price):
    """
    Faz o cálculo da metade de um preço.
    :param price: O preço.
    :return: O preço.
    """
    res = price / 2
    return res
