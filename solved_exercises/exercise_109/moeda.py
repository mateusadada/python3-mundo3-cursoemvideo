# Modifique as funções criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

def aumentar(price, percentage, formatting=False):
    """
    Aumenta um preço com base em uma porcentagem passada, além de poder retornar com a formatação R$ (real).
    :param price: O preço.
    :param percentage: A porcentagem.
    :param formatting: OPCIONAL - True ou False (padrão).
    :return: O preço.
    """
    res = price * (1 + percentage / 100)
    if formatting:
        res = moeda(res)
    return res


def diminuir(price, percentage, formatting=False):
    """
    Diminui um preço com base em uma porcentagem passada, além de poder retornar com a formatação R$ (real).
    :param price: O preço.
    :param percentage: A porcentagem.
    :param formatting: OPCIONAL - True ou False (padrão).
    :return: O preço.
    """
    res = price * (1 - percentage / 100)
    if formatting:
        res = moeda(res)
    return res


def dobro(price, formatting=False):
    """
    Faz o cálculo do dobro de um preço, além de poder retornar com a formatação R$ (real).
    :param price: O preço.
    :param formatting: OPCIONAL - True ou False (padrão).
    :return: O preço.
    """
    res = price * 2
    if formatting:
        res = moeda(res)
    return res


def metade(price, formatting=False):
    """
    Faz o cálculo da metade de um preço, além de poder retornar com a formatação R$ (real).
    :param price: O preço.
    :param formatting: OPCIONAL - True ou False (padrão).
    :return: O preço.
    """
    res = price / 2
    if formatting:
        res = moeda(res)
    return res


def moeda(price, coin='R$'):
    """
    Formata o preço na estrutura do real (R$) ou outro símbolo.
    :param price: O preço.
    :param coin: O símbolo da moeda (opcional e padrão: R$)
    :return: O preço.
    """
    return f'{coin}{price:.2f}'.replace('.', ',')
