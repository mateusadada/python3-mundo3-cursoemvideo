# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre
# a matriz na tela, com a formatação correta.

matriz = [[], [], []]

print('Bem-vindo ao programa que recebe os valores e exibe uma matriz 3x3!')

# preencher a matriz
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite um número para [{linha + 1}, {coluna + 1}]: ')))

# exibir a matriz
print(f'\n\033[33m*** MATRIZ 3x3 ***\033[m')
for posicao in matriz:
    for linha in range(3):
        print(f'[\033[33m{posicao[linha]:^5}\033[m] ', end='')
    print()
