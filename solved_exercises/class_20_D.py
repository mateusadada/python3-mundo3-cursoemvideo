def dobro(lista):
    for index, value in enumerate(lista):
        lista[index] = value * 2
    return lista


# main program
valores = [7, 2, 5, 0, 4]
print(valores)
# chama a função dentro do print
print(dobro(valores))
