# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista_total_numeros = [], []

print('Bem-vindo ao programa que exibe pares e ímpares de 7 valores inteiros em ordem crescente!')

for index in range(7):
    numero = int(input(f'{index + 1}º número: '))

    if numero % 2 == 0:
        lista_total_numeros[0].append(numero)
    else:
        lista_total_numeros[1].append(numero)

print(f'\nPares: \033[33m{sorted(lista_total_numeros[0])}\033[m'
      f'\nÍmpares: \033[33m{sorted(lista_total_numeros[1])}\033[m')
