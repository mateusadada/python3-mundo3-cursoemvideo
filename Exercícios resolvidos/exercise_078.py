# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

numeros = []

print('Bem-vindo ao programa que exibe o maior, o menor e a posição dos valores inteiros em uma lista!')

for index in range(5):
    numeros.append(int(input(f'{index + 1}º número: ')))

print(f'\nOs números digitados foram \033[33m{numeros}\033[m'
      f'\nMaior: \033[33m{max(numeros)} na posição {numeros.index(max(numeros)) + 1}\033[m'
      f'\nMenor: \033[33m{min(numeros)} na posição {numeros.index(min(numeros)) + 1}\033[m')
