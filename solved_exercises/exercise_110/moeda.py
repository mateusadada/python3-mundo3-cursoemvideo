# Adicione no módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
# informações geradas pelas funções que já temos no módulo criado até aqui.


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
    return f'{coin} {price:.2f}'.replace('.', ',')


def resumo(price, increase, decrease):
    """
    Exibe o resumo detalhado do preço.
    :param price: O preço.
    :param increase: A porcentagem de aumento.
    :param decrease: A porcentagem de redução.
    :return: Sem retorno. É mostrado na tela.
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(price)}')
    print(f'Dobro: \t\t\t\t{dobro(price, True)}')
    print(f'Metade: \t\t\t{metade(price, True)}')
    print(f'{increase}% de aumento: \t{aumentar(price, increase, True)}')
    print(f'{decrease}% de redução: \t{diminuir(price, decrease, True)}')
    print('-' * 30)
