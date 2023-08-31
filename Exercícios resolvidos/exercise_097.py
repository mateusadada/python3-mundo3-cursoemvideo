# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.
#
# Exemplo:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~

def write(text):
    print()
    size = len(text) + 4
    print('~' * size)
    print(f'  {text}')
    print('~' * size)


print('Bem-vindo ao programa que exibe uma mensagem com tamanho adaptável!')

write(str(input('Digite um texto qualquer: ')))
