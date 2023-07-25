# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = [0, 0, 0, 0, 0]

print('Bem-vindo ao programa exibe cinco valores ordenados!')

for index in range(5):
    numero = int(input(f'{index + 1}º número: '))
    lista[index] = numero

print(f'\nOs valores digitados ordenados são \033[33m{sorted(lista)}')
