"""Faça um programa que leia um número de 0 a 9999 e 
mostre na tela cada um dos dígitos separados.

Exemplo:  Digite um número: 1834
Unidade: 4 | Dezena: 3 | Centena: 8 | Milhar: 1"""

n1 = input('Digite um número entre 0 e 9999: ')

u = n1[-1]
d = n1[-2]
c = n1[-3] 
m = n1[-4]

print(f'Unidade: {u} | Dezena: {d} | Centena: {c} | Milhar: {m}')