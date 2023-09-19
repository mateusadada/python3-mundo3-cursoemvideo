# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS diferir de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar (35 anos de trabalho).

from datetime import datetime

trabalhador = dict()

print('Bem-vindo ao programa de cálculo de quantos anos a pessoa vai se aposentar!')

# recebe os dados e adiciona no dicionário
trabalhador['nome'] = str(input('Digite o nome: ')).strip().upper()
trabalhador['ano_de_nascimento'] = int(input('Ano de nascimento: '))
trabalhador['idade'] = int(datetime.today().year - trabalhador['ano_de_nascimento'])
trabalhador['CTPS'] = int(input('Número do CTPS (0 p/ vazio): '))
if trabalhador['CTPS'] != 0:
    trabalhador['ano_de_contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$ '))

# exibe os dados
print('\n*** Exibindo as informações do trabalhador ***'
      f'\nNome: \033[33m{trabalhador["nome"]}\033[m'
      f'\nAno de nascimento: \033[33m{trabalhador["ano_de_nascimento"]}\033[m'
      f'\nIdade: \033[33m{trabalhador["idade"]}\033[m')
if trabalhador['CTPS'] != 0:
    tempo_trabalhado = datetime.today().year - trabalhador['ano_de_contratacao']
    print(f'CTPS: \033[33m{trabalhador["CTPS"]}\033[m'
          f'\nAno de contratação: \033[33m{trabalhador["ano_de_contratacao"]}\033[m'
          f'\nSalário: \033[33mR$ {trabalhador["salario"]:.2f}\033[m'
          f'\nIrá se aposentar com \033[33m{35 - tempo_trabalhado + trabalhador["idade"]} anos em '
          f'{trabalhador["ano_de_contratacao"] + 35}\033[m')
