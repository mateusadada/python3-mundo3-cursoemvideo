filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }

print('\033[33m- Método interno que retorna os valores\033[m')
print(filme.values())

print()

print('\033[33m- Retorna as chaves\033[m')
print(filme.keys())

print()

print('\033[33m- Exibe as chaves e os valores; posso utilizar no for, parecido com o enumerate()\033[m')
print(filme.items())

print()

# for com items(); substituição ao enumerate() que usa com tuplas e listas
for key, value in filme.items():
    print(f'O {key} é {value}')

# print(locadora[0]['ano'])
