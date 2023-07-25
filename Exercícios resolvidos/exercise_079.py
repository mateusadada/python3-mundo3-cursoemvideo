# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

lista = []

print('Bem-vindo ao programa exibe os números digitados em ordem crescente!\n')

while True:
    numero = int(input('Digite um número inteiro (999 p/ sair): '))

    if numero == 999:
        break
    elif numero not in lista:
        lista.append(numero)

print(f'\nOs valores digitados em ordem crescente são \033[033m{sorted(lista)}')
