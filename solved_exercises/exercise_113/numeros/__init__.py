def leiaInt(text):
    """
    Permite apenas a inserção de um número inteiro.
    :param text: O texto.
    :return: O número.
    """
    while True:
        try:
            number_function = int(input(text))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return number_function


def leiaFloat(text):
    """
    Permite apenas a inserção de um número real.
    :param text: O texto.
    :return: O número.
    """
    while True:
        try:
            number_function = float(input(text))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return number_function
