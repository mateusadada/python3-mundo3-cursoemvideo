# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre
# a matriz na tela, com a formatação correta.

matriz = [[], [], []]

print('Bem-vindo ao programa que recebe os valores e exibe uma matriz 3x3!')

# preencher a matriz
for index in range(3):
    for index2 in range(3):
        numero = int(input(f'Digite um número para [{index + 1}, {index2 + 1}]: '))
        matriz[index].append(numero)

# exibir a matriz
print(f'\n\033[33m*** MATRIZ 3x3 ***\033[m', end='')
for posicao in matriz:
    print()
    for index in range(3):
        print(f'[\033[33m{posicao[index]:^5}\033[m] ', end='')

print()
