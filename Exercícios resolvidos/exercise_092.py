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
CTPS = int(input('Número do CTPS (0 p/ vazio): '))
if CTPS != 0:
    trabalhador['CTPS'] = CTPS
    trabalhador['ano_de_contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$ '))

# exibe os dados
print('\n*** Exibindo as informações do trabalhador ***'
      f'\nNome: {trabalhador["nome"]}'
      f'\nAno de nascimento: {trabalhador["ano_de_nascimento"]}'
      f'\nIdade: {trabalhador["idade"]}')
if CTPS != 0:
    print(f'CTPS: {trabalhador["CTPS"]}'
          f'\nAno de contratação: {trabalhador["ano_de_contratacao"]}'
          f'\nSalário: R$ {trabalhador["salario"]:.2f}'
          f'\nIrá se aposentar com XX anos no ano de XX')
