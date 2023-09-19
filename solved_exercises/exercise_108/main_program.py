from moeda import *

print('Bem-vindo ao programa de vários cálculos de moeda a partir de um valor!')
worth = float(input('Digite um preço: '))

print(f'\nA metade de {moeda(worth)} é {metade(worth)}'
      f'\nO dobro de {moeda(worth)} é {dobro(worth)}'
      f'\nAumentando 10% temos {aumentar(worth, 10)}')
