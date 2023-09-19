# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá conseguir mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.

def ficha(nome='<desconhecido>', quantos_gols=0):
    print(f'O jogador \033[33m{nome}\033[m fez \033[33m{quantos_gols}\033[m gol(s) no campeonato.')


# main program
print('Bem-vindo ao programa que exibe várias informações de um jogador!')
print('-' * 30)

nome_jogador = str(input('Nome do jogador: '))
numero_de_gols = str(input('Número de gols: '))

# validações e chamada da função ficha
if nome_jogador == '':
    if not numero_de_gols.isnumeric():
        ficha()
    else:
        ficha(quantos_gols=int(numero_de_gols))
else:
    if not numero_de_gols.isnumeric():
        ficha(nome_jogador)
    else:
        ficha(nome_jogador, int(numero_de_gols))
