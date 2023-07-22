# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

maior = menor = 0

print('Bem-vindo ao programa que gera cinco números aleatórios e exibe o maior e o menor!')

numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print(f'Números sorteados: \033[33m{numeros}\033[m')

for index in range(5):
    if index == 0:
        maior = menor = numeros[index]
    else:
        if numeros[index] > maior:
            maior = numeros[index]
        if numeros[index] < menor:
            menor = numeros[index]

print(f'\nMaior: \033[33m{maior}\033[m'
      f'\nMenor: \033[33m{menor}\033[m')
