# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um
# valor monetário formatado.

def aumentar(price, percentage):
    """
    Aumenta um preço com base em uma porcentagem passada, além de retornar com a formatação R$ (real).
    :param price: O preço.
    :param percentage: A porcentagem.
    :return: O preço formatado.
    """
    res = moeda(price * (1 + percentage / 100))
    return res


def diminuir(price, percentage):
    """
    Diminui um preço com base em uma porcentagem passada, além de retornar com a formatação R$ (real).
    :param price: O preço.
    :param percentage: A porcentagem.
    :return: O preço formatado. 
    """
    res = moeda(price * (1 - percentage / 100))
    return res


def dobro(price):
    """
    Faz o cálculo do dobro de um preço, além de retornar com a formatação R$ (real).
    :param price: O preço.
    :return: O preço formatado.
    """
    res = moeda(price * 2)
    return res


def metade(price):
    """
    Faz o cálculo da metade de um preço, além de retornar com a formatação R$ (real).
    :param price: O preço.
    :return: O preço formatado.
    """
    res = moeda(price / 2)
    return res


def moeda(price, coin='R$'):
    """
    Formata o preço na estrutura do real (R$) ou outro símbolo.
    :param price: O preço.
    :param coin: O símbolo da moeda (opcional e padrão: R$)
    :return: O preço formatado.
    """
    return f'{coin}{price:.2f}'.replace('.', ',')
