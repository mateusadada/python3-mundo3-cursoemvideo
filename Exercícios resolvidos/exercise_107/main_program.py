from moeda import *

print('Bem-vindo ao programa de vários cálculos de moeda a partir de um valor!')
worth = float(input('Digite um preço: R$ '))

print(f'\nA metade de R$ {worth:.2f} é R$ {metade(worth):.2f}'
      f'\nO dobro de R$ {worth:.2f} é R$ {dobro(worth):.2f}'
      f'\nAumentando 10% temos R$ {aumentar(worth, 10):.2f}')
