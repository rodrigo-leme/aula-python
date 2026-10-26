"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética). 
No final, mostre os 10 primeiros termos dessa progressão."""

i = int(input('Digite um número(primeiro termo): '))
p = int(input('Digite a razão: '))
# f = i + 10 * p

print(f'\nOs 10 primeiros termos da PA são: ')

for c in range(i, i + 10 * p, p):
    print(c, end= ' ')
