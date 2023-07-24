# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais.

print('Bem-vindo ao programa que exibe quais vogais tem uma palavra!')

palavras = ('crie', 'um', 'programa', 'que', 'tenha', 'uma', 'tupla', 'com', 'varias', 'palavras')
vogais = 'aeiou'

for word in palavras:
    print(f'\033[33m{word.upper()}\033[m tem ', end='')

    for worth in word:
        if worth.lower() in 'aeiou':
            print(f'\033[33m{worth}\033[m', end=' ')

    print()
