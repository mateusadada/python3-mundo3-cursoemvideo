# LISTAS são organizadas por índices
# DICIONÁRIOS são organizadores por palavras-chave

dados = list()
pessoas = list()

dados.append('Mateus')
dados.append(25)
print(dados[0])
print(dados[1])

print()
# adiciona uma lista (dois índices) dentro de outra
pessoas.append(dados[:])
print(pessoas[0])

print()
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
# o primeiro é qual o índice dentro da lista principal e o segundo é o índice dentro da lista
print(pessoas[2][0])
# mostra toda a lista
print(pessoas[1])
