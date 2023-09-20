def fatorial(numero):
    """
    Faz o cálculo do fatorial de um número.
    :param numero: O número.
    :return: O fatorial.
    """
    fat = 1
    for index in range(1, numero + 1):
        fat *= index
    return fat


def dobro(numero):
    """
    Faz o cálculo do dobro de um número.
    :param numero: O número.
    :return: O dobro do número.
    """
    return numero * 2


def triplo(numero):
    """
    Faz o cálculo do triplo de um número.
    :param numero: O número.
    :return: O triplo do número.
    """
    return numero * 3
