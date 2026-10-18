""" Refaça o Exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

EQUILÁTERO: todos os lados iguais

ISÓSCELES: dois lados iguais, um diferente

ESCALENO: todos os lados diferentes"""


a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if a + b <= c or a + c <= b or b + c <= a:
    print('As três retas NÃO podem formar um triângulo!')

elif a == b == c:
    print('As três retas formam um triângulo EQUILÁTERO!')

elif a == b or a == c or b == c:
    print('As três retas formam um triângulo ISÓSCELES!')

else:
    print('As três retas formam um triângulo ESCALENO!')