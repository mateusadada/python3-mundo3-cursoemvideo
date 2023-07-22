# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu
# programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

print('Bem-vindo ao programa que exibe um número entre 0 e 20 por extenso!')

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    usuario = int(input('Digite um número entre 0 e 20: '))

    if 0 <= usuario <= 20:
        break
    else:
        print('\033[31mEntrada inválida! Tente novamente.\033[m')

print(f'\nO número digitado foi \033[33m{numeros[usuario]}.')
