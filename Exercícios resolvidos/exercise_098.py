# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu
# programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, a cada 1
# b) de 10 até 0, a cada 2
# c) uma contagem personalizada

def line():
    print('-=' * 20)


# opcao A
def counter_1_until_10():
    line()
    print('Contagem de 1 até 10 de 1 em 1\033[33m')
    for index in range(1, 11):
        print(index, end=' ')
    print('FIM!\033[m')
    line()


# opção B
def counter_10_until_0():
    line()
    print('Contagem de 10 até 0 de 2 em 2\033[33m')
    for index in range(10, -1, -2):
        print(index, end=' ')
    print('FIM!\033[m')
    line()


# opção C
def custom_counter(start, stop, step):
    line()
    if step == 0:
        if start > stop:
            print(f'Contagem de {start} até {stop} de 1 em 1\033[33m')
            for index in range(start, stop - 1, - 1):
                print(index, end=' ')
            print('FIM!\033[m')

        elif start < stop:
            print(f'Contagem de {start} até {stop} de 1 em 1\033[33m')
            for index in range(start, stop + 1, 1):
                print(index, end=' ')
            print('FIM!\033[m')

        else:
            print('FIM!')

    elif start > stop:
        if step < 0:
            step = step * - 1

        print(f'Contagem de {start} até {stop} de {step} em {step}\033[33m')
        for index in range(start, stop - 1, - step):
            print(index, end=' ')
        print('FIM!\033[m')

    elif start < stop:
        if step < 0:
            step = step * - 1

        print(f'Contagem de {start} até {stop} de {step} em {step}\033[33m')
        for index in range(start, stop + 1, step):
            print(index, end=' ')
        print('FIM!\033[m')

    else:
        print('FIM!')


def main():
    print('Bem-vindo ao programa de cálculo de contagem!')
    counter_1_until_10()
    counter_10_until_0()

    print('Agora é a sua vez de personalizar a contagem!')
    start = int(input('Início: '))
    stop = int(input('Fim: '))
    step = int(input('Passo: '))
    custom_counter(start, stop, step)


main()
