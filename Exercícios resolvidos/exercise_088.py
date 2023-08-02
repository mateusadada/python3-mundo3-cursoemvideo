# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('Bem-vindo ao programa que cria vários palpites de 6 números entre 1 e 60!')

# quantidade de palpites
while True:
    quantidade_de_palpites = int(input('Digite a quantidade de palpites: '))

    if quantidade_de_palpites < 1:
        print('\033[31mEntrada inválida! Digite um número positivo. Tente novamente.\033[m')
    else:
        break

print(f'\n*** GERANDO OS {quantidade_de_palpites} PALPITES ***')
# cria a lista composta vazia
jogos = []
for index in range(quantidade_de_palpites):
    jogos.append([])

    # adiciona 6 números aleatórios únicos na lista composta
    for count in range(6):
        while True:
            sorteio = randint(1, 60)
            if sorteio not in jogos[index]:
                jogos[index].append(sorteio)
                break

    # exibe os palpites
    sleep(0.5)
    print(f'{index + 1}º jogo = \033[33m{sorted(jogos[index])}\033[m')
