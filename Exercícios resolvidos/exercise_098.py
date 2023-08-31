# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu
# programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, a cada 1
# b) de 10 até 0, a cada 2
# c) uma contagem personalizada

from time import sleep


def line():
    print('-=' * 20)


def custom_counter(start, stop, step):
    line()
    if step == 0:
        if start > stop:
            print(f'Contagem de {start} até {stop} de 1 em 1\033[33m')
            for value in range(start, stop - 1, - 1):
                sleep(0.3)
                print(value, end=' ')
            print('FIM!\033[m')

        elif start < stop:
            print(f'Contagem de {start} até {stop} de 1 em 1\033[33m')
            for value in range(start, stop + 1, 1):
                sleep(0.3)
                print(value, end=' ')
            print('FIM!\033[m')

        else:
            print('FIM!')

    elif start > stop:
        if step < 0:
            step = step * - 1

        print(f'Contagem de {start} até {stop} de {step} em {step}\033[33m')
        for value in range(start, stop - 1, - step):
            sleep(0.3)
            print(value, end=' ')
        print('FIM!\033[m')

    elif start < stop:
        if step < 0:
            step = step * - 1

        print(f'Contagem de {start} até {stop} de {step} em {step}\033[33m')
        for value in range(start, stop + 1, step):
            sleep(0.3)
            print(value, end=' ')
        print('FIM!\033[m')

    else:
        print('FIM!')


def main():
    print('Bem-vindo ao programa de cálculo de contagem!')
    custom_counter(1, 10, 1)
    custom_counter(10, 0, 2)

    line()
    print('Agora é a sua vez de personalizar a contagem!')
    start = int(input('Início: '))
    stop = int(input('Fim:    '))
    step = int(input('Passo:  '))
    custom_counter(start, stop, step)


main()
