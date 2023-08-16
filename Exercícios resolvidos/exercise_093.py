# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = dict()
gols = list()
total_gols = 0

print('Bem-vindo ao programa de cálculo do gerenciamento de um jogador de futebol!')

# recebe os dados e coloca no dicionário
dados['nome'] = str(input('Digite o nome do jogador: ')).strip().upper()
quantidade_partidas = int(input('Quantidade de partidas: '))
for index in range(quantidade_partidas):
    gols.append(int(input(f'Gols do {index + 1}º jogo: ')))
    total_gols += gols[index]
dados['gols_por_partida'] = gols
dados['total_gols'] = total_gols

# exibe os dados detalhadamente
print('=' * 30)
print(f'{dados}')
print('=' * 30)
print(f'Nome: \033[33m{dados["nome"]}\033[m'
      f'\nJogou \033[33m{quantidade_partidas}\033[m partidas e fez \033[33m{dados["total_gols"]}\033[m gols')
for index, value in enumerate(dados['gols_por_partida']):
    print(f'  - {index + 1}º jogo: \033[33m{value}\033[m')
