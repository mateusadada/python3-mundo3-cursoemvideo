# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Exemplo: n = leiaInt('Digite um n: ')

def leiaInt(number):
    """
    Permite apenas a inserção de um número natural.
    :param number: O número.
    :return: O número.
    """
    while True:
        number_function = input(number).strip()
        if number_function.isnumeric():
            return number_function
        else:
            print('\033[31mEntrada inválida! Digite um número natural válido.\033[m')


# main program
print('Bem-vindo ao programa que permite apenas valores numéricos!')
numero = leiaInt('Digite um número: ')
print(f'\nVocê acabou de digitar o número natural \033[33m{numero}\033[m.')
