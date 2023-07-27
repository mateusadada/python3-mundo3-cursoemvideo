# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

print('Bem-vindo ao programa que recebe e exibe cinco valores ordenados!')

for index in range(5):
    numero = int(input(f'{index + 1}º número: '))

    # adiciona o 1º valor na lista ou na última posição
    if index == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado no final da lista...')
    else:
        # verifica se tem algum valor menor e encaixa antes
        for index2 in range(len(lista)):
            if numero < lista[index2]:
                lista.insert(index2, numero)
                print(f'Adicionado na posição {index2 + 1} da lista...')
                break

print(f'\nOs valores digitados ordenados são \033[33m{lista}')
