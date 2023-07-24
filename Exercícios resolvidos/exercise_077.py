# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais.

print('Bem-vindo ao programa que exibe quais vogais tem uma palavra!')

palavras = ('crie', 'um', 'programa', 'que', 'tenha', 'uma', 'tupla', 'com', 'varias', 'palavras')
vogais = 'aeiou'

for word in palavras:
    print(f'\033[33m"{word}"\033[m tem ', end='')

    for worth in vogais:
        if worth in word:
            print(f'\033[33m{worth}\033[m', end=' ')

    print()
