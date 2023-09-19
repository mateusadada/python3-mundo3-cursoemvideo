# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dados em forma tabular.

print('Bem-vindo ao programa que exibe uma listagem de preços de produtos!\n')

produtos_e_precos = ('Escova dental', 4.75,
                     'Bolacha', 2.25,
                     'Mentos', 10.9,
                     'Café', 25.65,
                     'Carne bovina', 33.86)

print('=' * 34)
print('PRODUTO', ' ' * 17, 'PREÇO\n', end='')
print('=' * 34)

for index in range(0, len(produtos_e_precos)):
    if index % 2 == 0:
        print(f'{produtos_e_precos[index]:.<25}', end=' ')
    else:
        print(f'\033[33mR$ {produtos_e_precos[index]:>5.2f}\033[m')

print('=' * 34)
