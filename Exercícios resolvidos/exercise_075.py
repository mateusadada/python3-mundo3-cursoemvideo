# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

print('Bem-vindo ao programa que exibe várias informações a partir de quatro números informados!')

numero1 = int(input('1º número inteiro: '))
numero2 = int(input('2º número inteiro: '))
numero3 = int(input('3º número inteiro: '))
numero4 = int(input('4º número inteiro: '))
base_numeros = (numero1, numero2, numero3, numero4)
contador_valor_9 = int(0)
primeira_posicao_3 = str('')

# contador se aparecer o valor 9
for worth in base_numeros:
    if worth == 9:
        contador_valor_9 += 1

# primeira posição valor 3
for index, worth in enumerate(base_numeros):
    if worth == 3:
        primeira_posicao_3 = f'{index + 1}º'
        break
else:
    primeira_posicao_3 = 'Não foi digitado'

print(f'\nQuantas vezes apareceu o valor 9: \033[33m{contador_valor_9}\033[m'
      f'\nEm que posição foi digitado o primeiro valor 3: \033[33m{primeira_posicao_3}\033[m'
      f'\nQuais foram os números pares: \033[33m', end='')

# impressão números pares
for index, worth in enumerate(base_numeros):
    if worth % 2 == 0:
        print(worth, end=' ')
