# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um
# valor monetário formatado.

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
