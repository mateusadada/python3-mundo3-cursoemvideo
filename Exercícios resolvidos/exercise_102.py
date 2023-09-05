# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.

def factorial(number, show=False):
    """
    Performs the factorial calculation showing or not the calculation process on the screen.
    :param number: The number for the factorial.
    :param show: True to show and False not to show (default).
    :return: The factorial (with or without the calculation process).
    """
    sum_factorial = 1
    while number > 0:
        if show:
            print(number, end=' ')
            if number != 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        sum_factorial *= number
        number -= 1

    return sum_factorial


print('Bem-vindo ao programa de cálculo de fatorial mostrando ou não na tela o processo!')

print('-' * 30)
print(factorial(6, True))
