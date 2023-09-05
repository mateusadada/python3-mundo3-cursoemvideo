# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Exemplo: n = leiaInt('Digite um n: ')

def leiaInt(text):
    while True:
        number = input(text).strip()
        if number.isnumeric():
            return number
        else:
            print('\033[31mEntrada inválida! Digite um número natural válido.\033[m')


# main program
print('Bem-vindo ao programa que permite apenas valores numéricos!')

numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número \033[33m{numero}\033[m.')
