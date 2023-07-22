# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Grêmio.

print('Bem-vindo ao programa que exibe várias informações a partir da colocação do Campeonato Brasileiro de 2023!')

serie_A = ('Botafogo', 'Flamengo', 'Grêmio', 'São Paulo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Atlético-PR',
           'Fortaleza', 'Cruzeiro', 'Internacional', 'Atlético-MG', 'Cuiabá', 'Santos', 'Corinthians', 'Bahia',
           'Goiás', 'Coritiba', 'Vasco da Gama', 'América-MG')

print('\n\033[33m*** Os 5 primeiros times ***\033[m')
for index in range(5):
    print(f'{index + 1}º colocado: \033[33m{serie_A[index]}\033[m')

print('\n\033[33m*** Os últimos 4 colocados ***\033[m')
for index in range(16, 20):
    print(f'{index + 1}º colocado: \033[33m{serie_A[index]}\033[m')

print('\n\033[33m*** Times em ordem alfabética ***\033[m')
for index, name in enumerate(sorted(serie_A)):
    print(f'{index + 1}º: \033[33m{name}\033[m')

print('\n\033[33m*** Em que posição está o time do Grêmio ***\033[m')
for index, name in enumerate(serie_A):
    if name == 'Grêmio':
        print(f'O \033[33mGrêmio\033[m está na posição \033[33m{index + 1}\033[m')
