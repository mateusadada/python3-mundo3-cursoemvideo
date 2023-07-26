# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
# a expressão passada está com os parênteses abertos e fechados na ordem correta.

print('Bem-vindo ao programa que verifica se uma frase está com os parênteses na ordem correta!')

while True:
    expressao = str(input('Digite uma expressão matemática: '))

    if expressao.count('(') + expressao.count(')') < 1:
        print('\033[31mEntrada inválida! A expressão deve conter parênteses.\033[m')
    else:
        break

if expressao.count('(') == expressao.count(')'):
    print(f'\033[33mA expressão está correta!')
else:
    print(f'\033[31mA expressão NÃO está correta!')
