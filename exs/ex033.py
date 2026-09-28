"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))
n3 = float(input('Digite só mais um número: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é o maior')
else:
    print(f'{n3} é o maior')


if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor')
elif n2 < n1 and n2 < n3:
    print(f'{n2} é o menor')
else:
    print(f'{n3} é o menor')

##############################################################################

a = int(input('Primeirg valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é menor
menor = a
if bsa and b<c:
    menor = b
if csa and csb:
    menor = c
# Verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('0 menor valor digitado foi {}'. format(menor))
print('0 maior valor digitado foi {}'.format(maior))