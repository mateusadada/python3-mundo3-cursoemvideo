# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
# listas geradas.

lista_total = []
lista_pares = []
lista_impares = []

print('Bem-vindo ao programa que exibe três listas, uma de todos os números, outra dos pares e outra dos ímpares!')

while True:
    numero = int(input('Digite um número (999 p/ sair): '))

    if numero == 999:
        break
    else:
        lista_total.append(numero)

        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)

print(f'\nTodos os valores: \033[33m{lista_total}\033[m'
      f'\nPares: \033[33m{lista_pares}\033[m'
      f'\nÍmpares: \033[33m{lista_impares}\033[m')
