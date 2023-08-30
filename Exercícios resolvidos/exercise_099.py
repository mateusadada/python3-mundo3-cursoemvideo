# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu
# programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint
from time import sleep


def bigger(numbers_list):
    return max(numbers_list)


def line():
    print('-=' * 30)


def random_numbers():
    for index in range(6, 0, -1):
        print()
        line()

        print('Analisando os valores passados...'
              f'\nForam informados \033[33m{index}\033[m valores ao todo: \033[33m', end='')

        lista = list()
        for index2 in range(index):
            number = randint(0, 9)
            lista.append(number)
            sleep(0.3)
            print(lista[-1], end=' ')

        print(f'\n\033[mO maior valor gerado foi \033[33m{bigger(lista)}\033[m.')
        line()


print('Bem-vindo ao programa de cálculo do maior número!')

random_numbers()
