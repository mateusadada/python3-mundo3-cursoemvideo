valores = []

for index in range(5):
    valores.append(int(input(f'{index + 1}º valor: ')))

print()

for index, worth in enumerate(valores):
    print(f'{worth} na posição {index + 1}')

print('Cheguei ao final da lista.')
