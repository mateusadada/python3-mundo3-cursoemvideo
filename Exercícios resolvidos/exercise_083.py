# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
# a expressão passada está com os parênteses abertos e fechados na ordem correta.

parenteses_abertos = parenteses_fechados = 0

print('Bem-vindo ao programa que verifica se uma frase está com os parênteses na ordem correta!')

while True:
    expressao = str(input('Digite uma expressão matemática: ')).strip()

    if expressao.count('(') + expressao.count(')') < 1:
        print('\033[31mEntrada inválida! A expressão deve conter parênteses.\033[m')
    else:
        break

if expressao.count('(') == expressao.count(')'):
    for worth in expressao:
        if worth == '(':
            parenteses_abertos += 1
        elif worth == ')':
            parenteses_fechados += 1

        if parenteses_abertos < parenteses_fechados:
            print(f'\033[31mA expressão NÃO está correta!')
            break

    print(f'\033[33mA expressão está correta!')
else:
    print(f'\033[31mA expressão NÃO está correta!')
