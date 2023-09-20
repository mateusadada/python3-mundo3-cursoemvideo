from moeda import *

print('Bem-vindo ao programa de vários cálculos de moeda a partir de um valor!')
worth = float(input('Digite um preço: '))

print(f'\nA metade de {moeda(worth)} é {metade(worth, True)}'
      f'\nO dobro de {moeda(worth)} é {dobro(worth, True)}'
      f'\nAumentando 10% temos {aumentar(worth, 10, True)}'
      f'\nReduzindo 13% temos {diminuir(worth, 13, True)}')
