# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior.

from random import randint
from time import sleep


def raffle(numbers_list):
    print('Sorteando 5 valores e colocando na lista: \033[33m', end='')
    for index in range(5):
        sleep(0.3)
        numbers_list.append(randint(1, 10))
        print(numbers_list[-1], end=' ')
    sleep(0.3)
    print('PRONTO!\033[m')


def sum_of_pairs(numbers_list):
    sum_pairs = 0
    for value in numbers_list:
        if value % 2 == 0:
            sum_pairs += value

    sleep(0.3)
    print(f'Somando os valores pares de \033[33m{numbers_list}\033[m temos \033[33m{sum_pairs}\033[m.')


# main program
print('Bem-vindo ao programa de cálculo da soma de 5 números pares aleatórios!\n')
numbers = list()
raffle(numbers)
sum_of_pairs(numbers)
