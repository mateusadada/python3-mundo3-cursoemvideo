def linha(comprimento=42):
    return '-' * comprimento


def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for index, value in enumerate(lista):
        print(f'\033[33m{index + 1}\033[m - \033[36m{value}\033[m')
    print(linha())

    option = leiaInt('\033[33mSua opção: \033[m')
    return option


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
