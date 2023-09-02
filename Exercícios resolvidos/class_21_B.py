def somar(a=0, b=0, c=0):
    """
    Faz a soma de três valores (opcionais) e mostra o resultado na tela.
    :param a: O primeiro valor.
    :param b: O segundo valor.
    :param c: O terceiro valor.
    """
    soma = a + b + c
    print(f'A soma vale \033[33m{soma}\033[m')


somar(3, 2, 5)
somar(8, 4)
somar(17)
somar()
somar(c=9, a=-4, b=2)
