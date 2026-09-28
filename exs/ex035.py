"""Faça um programa que leia o comprimento de três retas
e diga se elas podem ou não formar um triângulo."""

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

# a soma de quaisquer dois lados precisa ser maior que o terceiro.
if a + b > c and a + c > b and b + c > a:
    print('As três retas podem formar um triângulo!')
else:
    print('As três retas NÃO podem formar um triângulo!')