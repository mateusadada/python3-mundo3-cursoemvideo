# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

jogadores_final = dict()
nome_resultado_jogadores = dict()
contador = 1

print('Bem-vindo ao programa que exibe quem foi o vencedor entre 4 jogadores de dados!')

for index in range(1, 5):
    # recebe o nome e o resultado do dado
    nome_resultado_jogadores['nome'] = str(input(f'Nome do {index}º: ')).strip()
    nome_resultado_jogadores['resultado'] = int(randint(1, 6))

    # adiciona no dicionário principal
    jogadores_final[f'jogador{index}'] = nome_resultado_jogadores.copy()

# imprime a classificação
print('\n=== RANKING DOS JOGADORES ===')
for value in sorted(jogadores_final.items(), key=lambda x: x[1]['resultado'], reverse=True):
    sleep(1)
    print(f'{contador}º lugar:\033[33m {value[1]["nome"]} com {value[1]["resultado"]} pontos\033[m')
    contador += 1
