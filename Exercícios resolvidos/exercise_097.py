# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.
#
# Exemplo:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~

def escreva(texto):
    print()
    print('~' * len(texto))
    print(texto)
    print('~' * len(texto))


print('Bem-vindo ao programa que exibe uma mensagem com tamanho adaptável!')
escreva(str(input('Digite um texto qualquer: ')))
