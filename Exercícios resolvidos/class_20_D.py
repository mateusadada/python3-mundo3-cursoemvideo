def dobro(lista):
    for index, value in enumerate(lista):
        lista[index] = value * 2
    return lista


valores = [7, 2, 5, 0, 4]
print(valores)
print(dobro(valores))
