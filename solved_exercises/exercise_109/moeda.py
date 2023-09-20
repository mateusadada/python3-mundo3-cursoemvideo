# Modifique as funções criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

def aumentar(price, percentage):
    res = moeda(price * (1 + percentage / 100))
    return res


def diminuir(price, percentage):
    res = moeda(price * (1 - percentage / 100))
    return res


def dobro(price):
    res = moeda(price * 2)
    return res


def metade(price):
    res = moeda(price / 2)
    return res


def moeda(price, coin='R$'):
    return f'{coin}{price:.2f}'.replace('.', ',')
