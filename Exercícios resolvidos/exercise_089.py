# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
# um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista_alunos = []

# print('Bem-vindo ao programa que gera e exibe o boletim de várias alunos!')

# validação de quantos alunos
while True:
    quantidade = int(input('Deseja incluir quantos alunos? '))

    if quantidade < 1:
        print('\033[31mEntrada inválida. Digite um número positivo. Tente novamente.\033[m')
    else:
        break

for index in range(quantidade):
    # cria um espaço vazio na lista composta
    lista_alunos.append([])

    # recebe os dados e adiciona na lista composta
    lista_alunos[index].append(str(input(f'\nNome do {index + 1}º aluno: ')).strip().upper())
    lista_alunos[index].append(float(input('1º nota: ')))
    lista_alunos[index].append(float(input('2º nota: ')))
    lista_alunos[index].append(float((lista_alunos[index][1] + lista_alunos[index][2]) / 2))

    print(lista_alunos[index])
    print(lista_alunos)
