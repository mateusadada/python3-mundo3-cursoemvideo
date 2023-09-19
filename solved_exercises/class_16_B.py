lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

print(lanche[-2::-1])

# lanche[1] = ('Refrigerante') não é permitido, pois é imutável

print(lanche[1], '\n\033[33m')

print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')

print()

for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]}')
