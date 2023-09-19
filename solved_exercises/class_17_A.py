# listas são mutáveis

numeros = [2, 5, 9, 1]
numeros[2] = 3
numeros.append(7)
numeros.sort(reverse=True)
numeros.insert(2, 2)
# elimina a primeira ocorrência; posso fazer um if ou for para eliminar vários
numeros.remove(2)
# elimina o último valor ou informo o índice
# numeros.pop(2)

print(numeros)
print(f'Essa lista tem {len(numeros)} elementos.')
