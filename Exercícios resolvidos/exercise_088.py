# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

# jogos = [[xxxxxx], [xxxxxx], ...]

# print('Bem-vindo ao programa que cria vários palpites de 6 números entre 1 e 60!')

# colocar num while True
quantidade_de_palpites = int(input('Digite a quantidade de palpites: '))

# cria a lista vazia
jogos = list(range(quantidade_de_palpites))

for index in range(6):

