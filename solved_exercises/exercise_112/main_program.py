# from solved_exercises.exercise_112.utilidadesCeV.dado import leiaDinheiro
# from solved_exercises.exercise_112.utilidadesCeV.moeda import resumo
from utilidadesCeV.dado import leiaDinheiro
from utilidadesCeV.moeda import resumo

print('Bem-vindo ao programa que exibe uma lista detalhada e organizada a partir de um valor!')
price = leiaDinheiro('Digite um preço: R$ ')
resumo(price, 80, 35)
