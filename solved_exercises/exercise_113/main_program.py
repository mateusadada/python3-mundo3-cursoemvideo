# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
# de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from numeros import *

print('Bem-vindo ao programa que permite a digitação, um de cada vez, apenas de números inteiros e reais!')

numero_inteiro = leiaInt('Digite um INTEIRO: ')
numero_real = leiaFloat('Digite um REAL: ')

print(f'\nO valor inteiro digitado foi \033[33m{numero_inteiro}\033[m e o real \033[33m{numero_real}\033[m')
