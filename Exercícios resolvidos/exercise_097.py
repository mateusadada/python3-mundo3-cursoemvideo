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
    print('~' * (len(text) + 4))
    print(f'  {text}')
    print('~' * (len(text) + 4))


print('Bem-vindo ao programa que exibe uma mensagem com tamanho adaptável!')

write(str(input('Digite um texto qualquer: ')))
