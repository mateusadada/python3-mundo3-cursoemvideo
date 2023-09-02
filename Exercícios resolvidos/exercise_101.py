# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date


def vote(year_of_birth=0):
    """
    Returns a literal value indicating whether a person in voting denied, optional, or required, in addition to age.
    :param year_of_birth: The voter's year of birth.
    :return: Age and whether voting is denied, optional, or required.
    """
    age = date.today().year - year_of_birth

    if year_of_birth == 0:
        return '\033[31mIDADE INVÁLIDA.\033[m'
    else:
        print(f'Com {age} anos: ', end='')
        if 16 <= age < 18 or age >= 60:
            return '\033[33mVOTO OPCIONAL.\033[m'
        elif 18 <= age < 60:
            return '\033[32mVOTO OBRIGATÓRIO.\033[m'
        else:
            return '\033[31mVOTO NEGADO.\033[m'


print('Bem-vindo ao programa de verificação da situação de um eleitor!\n')

year = int(input('Em que ano você nasceu? '))
print(vote(year))
