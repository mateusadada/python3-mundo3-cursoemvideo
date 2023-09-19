# cria a lista das características
pessoa = list()
pessoa.append('Mateus')
pessoa.append(21)

# cria a lista galera que engloba a lista pessoa
galera = list()
galera.append(pessoa[:])

# faz modificações na lista primária pessoa
pessoa[0] = 'Julia'
pessoa[1] = 20

print(galera)

# adiciono novamente a lista primária
galera.append(pessoa[:])

print(galera)
