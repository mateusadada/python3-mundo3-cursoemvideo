# Existem 3 variáveis compostas: tuplas, listas e dicionários
# Tupla: guarda valores imutáveis acessíveis por chaves individuais

lanche = ('hambúrguer', 'Suco', 'Pizza', 'Pudim', 456, 10.4)

print(lanche[-4])
print(len(lanche), '\n')

for comida in lanche:
    print(comida)
