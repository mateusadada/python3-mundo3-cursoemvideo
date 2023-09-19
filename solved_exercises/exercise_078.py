# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

lista_numeros = []

print('Bem-vindo ao programa que exibe o maior, o menor e a posição de 5 valores inteiros em uma lista!')

for index in range(5):
    lista_numeros.append(int(input(f'{index + 1}/5 número: ')))

print(f'\nOs números digitados foram \033[33m{lista_numeros}\033[m'
      f'\nMaior: \033[33m{max(lista_numeros)} nas posições ', end='')
for index, worth in enumerate(lista_numeros):
    if worth == max(lista_numeros):
        print(index + 1, end=' ')

print(f'\n\033[mMenor: \033[33m{min(lista_numeros)} nas posições ', end='')
for index, worth in enumerate(lista_numeros):
    if worth == min(lista_numeros):
        print(index + 1, end=' ')
