import math 
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'a raiz de {num} é igual a {raiz}')
print(f'a raiz de {num} é igual a {math.ceil(raiz)}') #método ceil de math, faz o arredondamento para cima
print(f'a raiz de {num} é igual a {math.floor(raiz)}') #método floor de math, faz o arredondamento para baixo

#######################################################

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'a raiz de {num} é igual a {floor(raiz):.2f}')

