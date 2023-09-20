import moeda

print('Bem-vindo ao programa de vários cálculos de moeda a partir de um valor!')
worth = float(input('Digite um preço: '))

print(f'\nA metade de {moeda.moeda(worth)} é {moeda.metade(worth)}'
      f'\nO dobro de {moeda.moeda(worth)} é {moeda.dobro(worth)}'
      f'\nAumentando 10% temos {moeda.aumentar(worth, 10)}')
