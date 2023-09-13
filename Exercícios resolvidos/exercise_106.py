# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

from time import sleep


def lines(text):
    """
    Imprime o texto com o símbolo '~' tanto em cima quanto embaixo.
    :param text: O texto.
    :return: Sem retorno.
    """
    length = len(text)
    print('~' * (length + 4))
    print(f'  {text}')
    print('~' * (length + 4))


# main program
print('Bem-vindo ao programa que exibe a ajuda (HELP) do Python!')

while True:
    print('\033[30:42m', end='')
    lines('SISTEMA DE AJUDA PyHELP')
    print('\033[m')

    user = str(input('Função ou biblioteca (FIM p/ sair) > ')).strip()
    sleep(0.5)

    if user in 'FIMfim':
        print('\033[41m', end='')
        lines('ATÉ LOGO!')
        break

    print('\033[30:45m', end='')
    lines(f"Acessando o manual do comando '{user}'")

    sleep(0.5)
    print('\033[47m')
    help(user)
    sleep(1)
