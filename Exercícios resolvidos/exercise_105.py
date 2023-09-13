# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(*note, situation=False):
    """
    Coloca dentro do dicionário informações a partir de várias notas (sem limites): quantidade, maior, menor, média
    e a situação (opcional).
    :param note: As notas.
    :param situation: True para mostrar (BOA, REGULAR ou RUIM) e False para não exibir (padrão).
    :return: Um dicionário com as informações.
    """
    data = {'quantidade_notas': len(note),
            'maior': max(note),
            'menor': min(note),
            'media': sum(note) / len(note)}

    if situation:
        if data['media'] >= 7:
            data['situação'] = 'BOA'
        elif data['media'] < 5:
            data['situação'] = 'RUIM'
        else:
            data['situação'] = 'REGULAR'

    return data


# main program
print('Bem-vindo ao programa de cálculo que exibe várias informações a partir das notas de um aluno!'
      '\nNotas: \033[33m5.5, 2.5, 10, 6.5 e 9\033[m')
print('-' * 30)

notas_aluno = notas(5.5, 2.5, 10, 6.5, 9, situation=True)
print(notas_aluno)
