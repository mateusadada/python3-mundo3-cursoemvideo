# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

from time import sleep


def lines(text, font=0, background=0):
    """
    Imprime o texto com o símbolo '~' tanto em cima quanto embaixo com cores.
    :param text: O texto.
    :param font: O código da fonte.
    :param background: O código do fundo.
    :return: Sem retorno.
    """
    length = len(text) + 4
    print(f'\033[{font}:{background}m', end='')
    print('~' * length)
    print(f'  {text}')
    print('~' * length)
    print('\033[m', end='')


# main program
print('Bem-vindo ao programa que exibe a ajuda (HELP) do Python!')

while True:
    lines('SISTEMA DE AJUDA PyHELP', 30, 42)

    user = str(input('Função ou biblioteca (FIM p/ sair) > ')).strip()
    sleep(0.5)

    if user.upper() in 'FIM':
        lines('ATÉ LOGO!', background=41)
        break

    lines(f"Acessando o manual do comando '{user}'", 30, 45)

    sleep(0.5)
    print('\033[47m')
    help(user)
    print('\033[m', end='')
    sleep(1)
