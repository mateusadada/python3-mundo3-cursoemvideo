# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dados em forma tabular.

print('Bem-vindo ao programa que exibe uma listagem de preços de produtos!\n')

produtos_e_precos = ('Escova dental', 4.75, 'Bolacha', 2.25, 'Mentos', 10.9, 'Café', 25.65, 'Carne bovina', 33.86)

print('PRODUTO', ' ' * 17, 'PREÇO\n', end=''
      '-' * 33)
print()

for index, worth in enumerate(produtos_e_precos):
    if index % 2 == 0:
        print(f'{worth:25}', end=' ')
    else:
        print(f'\033[33mR$ {worth:5.2f}\033[m')
