# Aprimore o desafio anterior (exercise_086), mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[], [], []]
pares = soma_3_coluna = 0

print('Bem-vindo ao programa exibe várias informações a partir de uma matriz 3x3!')

# preencher a matriz
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite um número para [{linha + 1}, {coluna + 1}]: ')))

# exibir a matriz
print(f'\n\033[33m*** MATRIZ 3x3 ***\033[m')
for index, posicao in enumerate(matriz):
    for linha in range(3):
        print(f'[\033[33m{posicao[linha]:^5}\033[m] ', end='')

        # opção A
        if posicao[linha] % 2 == 0:
            pares += posicao[linha]

        # opção B
        if linha == 2:
            soma_3_coluna += posicao[linha]
    print()

print(f'\n- A soma de todos os pares é \033[33m{pares}\033[m.'
      f'\n- A soma da terceira coluna é \033[33m{soma_3_coluna}\033[m.'
      f'\n- O maior valor da segunda linha é \033[33m{max(matriz[1])}\033[m.')
