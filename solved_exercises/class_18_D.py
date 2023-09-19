galera = []
dado = []

for index in range(3):
    dado.append(str(input(f'\n{index + 1}º nome: ')).strip())
    dado.append(int(input('Idade: ')))

    galera.append(dado[:])

    dado.clear()

print()
for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'\033[32m{pessoa[0]} é maior de idade.')
    else:
        print(f'\033[33m{pessoa[0]} NÃO é maior de idade.')
