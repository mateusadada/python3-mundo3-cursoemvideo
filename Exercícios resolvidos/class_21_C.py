def test():
    # escopo local
    x = 8
    print(f'Na função teste, numero vale {numero}')
    print(f'Na função teste, x vale {x}')


# main program
# escopo global
numero = 2
print(f'No programa principal, número vale {numero}')
test()
