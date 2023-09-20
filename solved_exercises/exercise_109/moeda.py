# Modifique as funções criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

def aumentar(price, percentage, formatting=False):
    res = price * (1 + percentage / 100)
    if formatting:
        res = moeda(res)
    return res


def diminuir(price, percentage, formatting=False):
    res = price * (1 - percentage / 100)
    if formatting:
        res = moeda(res)
    return res


def dobro(price, formatting=False):
    res = price * 2
    if formatting:
        res = moeda(res)
    return res


def metade(price, formatting=False):
    res = price / 2
    if formatting:
        res = moeda(res)
    return res


def moeda(price, coin='R$'):
    return f'{coin}{price:.2f}'.replace('.', ',')
