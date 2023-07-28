# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista_nomes_e_pesos = list()
lista_auxiliar = list()
contador_de_pessoas = 0

print('Bem-vindo ao programa que exibe várias informações a partir do peso de várias pessoas!', end='')

while True:
    # variáveis e adicionando na lista auxiliar
    lista_auxiliar.append(str(input('\nDigite o nome: ')).strip())
    lista_auxiliar.append(float(input('Peso: ')))

    # opção A
    contador_de_pessoas += 1

    # adicionar na lista principal de maneira independente
    lista_nomes_e_pesos.append(lista_auxiliar[:])

    # apagar a lista auxiliar
    lista_auxiliar.clear()

    # validação da continuação
    while True:
        continuar = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]

        if continuar not in 'SN':
            print('\033[31mEntrada inválida! Digite "sim" ou "não". Tente novamente.\033[m')
        else:
            break

    # sair do while True
    if continuar == 'N':
        break

# print das informações solicitadas
# opção A
print(f'\nForam cadastradas \033[33m{contador_de_pessoas}\033[m pessoa(s).')

# opção B
print(f'Listagem das pessoas mais pesadas com \033[33m{max(lista_nomes_e_pesos)[1]} kg: ', end='')
for pessoa in lista_nomes_e_pesos:
    if pessoa[1] == max(lista_nomes_e_pesos)[1]:
        print(pessoa[0], end='')

# opção C
print(f'\n\033[mListagem das pessoas mais leves com \033[33m{min(lista_nomes_e_pesos)[1]} kg: ', end='')
for pessoa in lista_nomes_e_pesos:
    if pessoa[1] == min(lista_nomes_e_pesos)[1]:
        print(pessoa[0], end='')
