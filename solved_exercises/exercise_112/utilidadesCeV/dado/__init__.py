# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
# leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar
# apenas valores que seja monetários.

def leiaDinheiro(text):
    """
    Validação de dados que permite apenas a entrada de valores monetários (decimal permite com ponto ou vírgula).
    :param text: Mensagem que aparece no input para o usuário.
    :return: O valor no formato float.
    """
    while True:
        entry = str(input(text)).replace(',', '.').strip()

        if entry.isalpha() or entry == '':
            print(f'\033[31mERRO: "{entry}" é um preço inválido!\033[m')
        else:
            return float(entry)
