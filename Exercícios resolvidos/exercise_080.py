# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

print('Bem-vindo ao programa que recebe e exibe cinco valores ordenados!')

for index in range(5):
    numero = int(input(f'{index + 1}º número: '))

    # adiciona o 1º valor na lista
    if len(lista) < 1:
        lista.append(numero)
    else:
        # verifica se tem algum valor menor e encaixa antes
        for index2 in range(len(lista)):
            if numero < lista[index2]:
                lista.insert(index2, numero)
                break
        else:
            lista.append(numero)

print(f'\nOs valores digitados ordenados são \033[33m{lista}')
