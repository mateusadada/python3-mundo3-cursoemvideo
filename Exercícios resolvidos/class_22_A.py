# Modularização: dividir um programa grande, aumentar a legibilidade e facilitar a manutenção.

# Módulo: arquivo.py com conjunto de funções.
# Pacote/biblioteca: conjunto de módulos; separados por assunto.

from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')
