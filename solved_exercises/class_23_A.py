# exceção: erros

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# não é recomendável especificar o tipo de erro, pois torna mais vulnerável a ataques
# posso mostrar o tipo de erro no desenvolvimento para me ajudar
# posso ter vários Exception (erros)

# except (ValueError, TypeError) :
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
# opcional
else:
    print(f'O resultado é {r:.1f}')
# opcional
finally:
    print('Volte sempre! Muito obrigado!')
