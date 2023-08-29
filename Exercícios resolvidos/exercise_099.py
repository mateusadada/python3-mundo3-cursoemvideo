# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu
# programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* numero):
    return max(numero)


print('Bem-vindo ao programa de cálculo do maior número!')

print('\nNúmeros: 2, 5, 9, 2, 45, 7, 5, 35, 45, -87, 54'
      f'\nMaior: \033[33m{maior(2, 5, 9, 2, 45, 7, 5, 35, 45, -87, 54)}')
