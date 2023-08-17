# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

lista_das_pessoas = list()
total_idade = media_idade = 0

# print('Bem-vindo ao programa que exibe várias informações a partir do nome, sexo e idade de várias pessoas!')

# recebe os dados e organiza na lista
while True:
    # recebe os dados
    nome = str(input('\nDigite o nome: ')).strip().upper()
    # validação do sexo
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo not in 'MF':
            print('\033[31mEntrada inválida! Digite "M" ou "F". Tente novamente.\033[m')
        else:
            break
    idade = int(input('Idade: '))

    # adiciona no dicionário geral
    dados_da_pessoa = {'nome': nome,
                       'sexo': sexo,
                       'idade': idade}

    # faz uma cópia do dicionário geral do dicionário único
    dados_da_pessoa[f'{len(lista_das_pessoas)}'] = dados_da_pessoa.copy()

    # adiciona o dicionário único na lista
    lista_das_pessoas.append(dados_da_pessoa[f'{len(lista_das_pessoas)}'])

    # limpa o dicionário geral
    dados_da_pessoa.clear()

    # validação se quer continuar
    while True:
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if continuar not in 'SN':
            print('\033[31mEntrada inválida! Digite "S" ou "N". Tente novamente.\033[m')
        else:
            break
    if continuar == 'N':
        break

# exibir os dados detalhados
# opção A
print('\n*** EXIBINDO OS DADOS DETALHADOS ***'
      f'\nA) Foram cadastradas {len(lista_das_pessoas)} pessoas')

# opção B
for items in lista_das_pessoas:
    total_idade += items['idade']
media_idade = total_idade / len(lista_das_pessoas)
print(f'B) A média de idade é de {media_idade:.1f} anos')

# opção C
print('C) As mulheres cadastradas foram ', end='')
for items in lista_das_pessoas:
    if items['sexo'] == 'F':
        print(items['nome'], end=' ')
print()

# opção D
