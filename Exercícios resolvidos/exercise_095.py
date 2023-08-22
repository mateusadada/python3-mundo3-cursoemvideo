# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.

lista_jogadores = list()
dados_jogador = dict()
gols = list()
mostrar_jogador = 0

print('Bem-vindo ao programa de cálculo do gerenciamento de vários jogadores de futebol!', end='')

while True:
    # limpa, recebe os dados e coloca no dicionário
    gols.clear()
    dados_jogador['nome'] = str(input('\nDigite o nome do jogador: ')).strip().upper()
    quantidade_partidas = int(input('Quantidade de partidas: '))
    for index in range(quantidade_partidas):
        gols.append(int(input(f'Gols do {index + 1}º jogo: ')))
    dados_jogador['gols_por_partida'] = gols[:]
    dados_jogador['total_gols'] = sum(gols)

    # coloca na lista as informações do jogador
    lista_jogadores.append(dados_jogador.copy())

    # validação se deseja continuar
    while True:
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if continuar not in 'SN':
            print('\033[31mEntrada inválida! Digite "SIM" ou "NÃO". Tente novamente.\033[m')
        else:
            break

    if continuar == 'N':
        print()
        break


# exibe os dados detalhadamente
print('=' * 50)
print('Cód Nome           Gols         Total')
print('-' * 38)
for index, value in enumerate(lista_jogadores):
    print(f'{index:>3} {value["nome"]:<14} {value["gols_por_partida"]} {value["total_gols"]}')
print('-' * 38)
print('=' * 50)

while mostrar_jogador != 999:
    mostrar_jogador = int(input('\nMostrar os dados de qual jogador (999 p/ parar): '))
    if mostrar_jogador != 999:
        print(f'-- LEVANTAMENTO DO JOGADOR \033[33m{lista_jogadores[mostrar_jogador]["nome"]}\033[m --')
        for index, value in enumerate(lista_jogadores[mostrar_jogador]["gols_por_partida"]):
            print(f'  - {index + 1}º jogo: \033[33m{value} gols\033[m')
    else:
        print('\nSaindo do programa. Até logo!')
