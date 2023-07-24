# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

print('Bem-vindo ao programa que exibe várias informações a partir de quatro números informados!')

base_numeros = (int(input('1º número inteiro: ')),
                int(input('2º número inteiro: ')),
                int(input('3º número inteiro: ')),
                int(input('4º número inteiro: ')))

print(f'\nQuantas vezes apareceu o valor 9: \033[33m{base_numeros.count(9)}\033[m')

if 3 in base_numeros:
    print(f'O primeiro valor 3 está na \033[33m{base_numeros.index(3) + 1}º\033[m posição')
else:
    print('Não foi digitado o valor 3')

print(f'Os valores pares foram: \033[33m', end='')
for worth in base_numeros:
    if worth % 2 == 0:
        print(worth, end=' ')
