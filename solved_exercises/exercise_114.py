# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request

print('Bem-vindo ao programa que teste se o site PUDIM está online!')

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O site Pudim \033[31mNÃO\033[m está acessível no momento!')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
