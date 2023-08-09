# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre
# o conteúdo da estrutura na tela.

dados_aluno = dict()

print('Bem-vindo ao programa que exibe o nome e a média de um aluno guardado em um dicionário!')

# lê os dados
dados_aluno['nome'] = str(input('Digite o nome: ')).strip()
dados_aluno['media'] = float(input('Digite a média: '))

# cálculo da situação
if dados_aluno['media'] >= 7:
    situacao = 'Aprovado'
elif dados_aluno['media'] < 5:
    situacao = 'Reprovado'
else:
    situacao = 'Recuperação'

dados_aluno['situacao'] = situacao

# exibe o conteúdo
print(f'\nExibindo a estrutura do dicionário: \033[33m{dados_aluno}')
