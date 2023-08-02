# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
# um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

# print('Bem-vindo ao programa que gera e exibe o boletim de várias alunos!')

# validação de quantos alunos
while True:
    quantidade = int(input('Deseja incluir quantos alunos? '))

    if quantidade < 1:
        print('\033[31mEntrada inválida. Digite um número positivo. Tente novamente.\033[m')
    else:
        break

# cadastro
dados_alunos = []
for index in range(quantidade):
    # cria um espaço vazio na lista composta
    dados_alunos.append([])

    # recebe os dados e adiciona na lista composta
    dados_alunos[index].append(str(input(f'\nNome do {index + 1}º aluno: ')).strip().upper())
    dados_alunos[index].append(float(input('1º nota: ')))
    dados_alunos[index].append(float(input('2º nota: ')))
    dados_alunos[index].append(float((dados_alunos[index][1] + dados_alunos[index][2]) / 2))

# exibir o boletim
print(f'\n\033[33m*** BOLETIM DOS {quantidade} ALUNOS ***\033[m'
      f'\nCód. Nome')
for index in range(quantidade):
    print(f'{index + 1:<5}', end='')
    print(f'{dados_alunos[index][0]:<25}', end='')
    print(f'{dados_alunos[index][3]:.1f}')
