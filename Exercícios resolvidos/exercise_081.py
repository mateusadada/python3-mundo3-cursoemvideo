# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

print('Bem-vindo ao programa que exibe várias informações a partir de números informados!')

while True:
    numero = int(input('Digite um número (999 p/ sair): '))

    if numero == 999:
        break
    else:
        lista.append(numero)

print(f'\nQuantos números foram digitados: \033[33m{len(lista)}\033[m'
      f'\n*** A lista ordenada de forma decrescente ***'
      f'\n\033[33m{sorted(lista, reverse=True)}\033[m'
      f'\nO valor 5 foi digitado? \033[33m', end='')
if 5 in lista:
    print(f'Sim, na posição {lista.index(5) + 1}')
else:
    print('Não')
