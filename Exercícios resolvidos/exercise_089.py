# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
# um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

print('Bem-vindo ao programa que gera e exibe o boletim de várias alunos!')

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
print(f'\n\033[33m *** BOLETIM DOS {quantidade} ALUNOS ***\033[m')
print('-' * 30)
print(f'Cód. Nome                Média')
for index in range(quantidade):
    print(f'{index:<5}', end='')
    print(f'{dados_alunos[index][0]:<20}', end='')
    print(f'{dados_alunos[index][3]:.1f}')
print('-' * 30)

# exibir as notas detalhadas
while True:
    # validação para mostrar alunos válidos
    while True:
        ver_notas = int(input(f'\nDeseja ver as notas de qual aluno (cód. 0 a {quantidade - 1})? '))

        if ver_notas < 0 or ver_notas >= quantidade:
            print('\033[31mEntrada inválida. Digite um número válido. Tente novamente.\033[m', end='')
        else:
            print(f'Nome: \033[33m{dados_alunos[ver_notas][0]}\033[m (cód. {ver_notas})'
                  f'\n1º nota: \033[33m{dados_alunos[ver_notas][1]:.1f}\033[m'
                  f'\n2º nota: \033[33m{dados_alunos[ver_notas][2]:.1f}\033[m')
            break

    # validação da continuação
    while True:
        continuar = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]

        if continuar not in 'SN':
            print('\033[31mEntrada inválida! Digite "sim" ou "não". Tente novamente.\033[m')
        else:
            break

    # sair do main loop
    if continuar == 'N':
        break
