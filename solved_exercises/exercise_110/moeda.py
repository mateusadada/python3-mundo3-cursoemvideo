# Adicione no módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
# informações geradas pelas funções que já temos no módulo criado até aqui.


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
    return f'{coin} {price:.2f}'.replace('.', ',')


def resumo(price, increase, decrease):
    print('-' * 30)
    print('       RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado: {moeda(price):>12}')
    print(f'Dobro: {dobro(price, True):>22}')
    print(f'Metade: {metade(price, True):>21}')
    print(f'{increase}% de aumento: {aumentar(price, increase, True):>13}')
    print(f'{decrease}% de redução: {diminuir(price, decrease, True):>13}')
    print('-' * 30)
