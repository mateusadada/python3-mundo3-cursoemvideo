# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre
# o conteúdo da estrutura na tela.

dados_aluno = dict()

print('Bem-vindo ao programa que exibe o nome e a média de um aluno guardado em um dicionário!')

# lê os dados
dados_aluno['nome'] = str(input('Digite o nome: ')).strip()
dados_aluno['media'] = float(input(f'A média de {dados_aluno["nome"]}: '))

# cálculo da situação
if dados_aluno['media'] >= 7:
    dados_aluno['situacao'] = 'Aprovado'
elif dados_aluno['media'] < 5:
    dados_aluno['situacao'] = 'Reprovado'
else:
    dados_aluno['situacao'] = 'Recuperação'

# exibe o conteúdo
print(f'\nExibindo a estrutura do dicionário: \033[33m{dados_aluno}\033[m')

# exibe o conteúdo detalhado
print(f'\nExibindo a estrutura organizada:')
for key, value in dados_aluno.items():
    print(f'- {key} é \033[33m{value}\033[m')
