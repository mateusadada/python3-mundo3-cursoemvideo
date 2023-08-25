# Empacotamento: o símbolo * indica que vai haver vários parâmetros, mas não sei quantos
# Vou mandar empacotado e a função irá desempacotar

def contador(* num):
    # vira uma TUPLA
    for value in num:
        print(value, end=' ')
    print(f'FIM - Tamanho -> {len(num)}')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
