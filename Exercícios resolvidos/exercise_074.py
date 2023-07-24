# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

print('Bem-vindo ao programa que gera cinco números aleatórios e exibe o maior e o menor!')

numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print(f'\nNúmeros sorteados: \033[33m', end='')
for worth in numeros:
    print(worth, end=' ')

print(f'\n\033[mMaior: \033[33m{max(numeros)}\033[m'
      f'\nMenor: \033[33m{min(numeros)}\033[m')
