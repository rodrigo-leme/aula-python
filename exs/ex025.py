"""Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome"""

nome = input('Digite seu nome: ')

if nome.find('Silva'):
    print('seu nome possui Silva')
else:
    print('seu nome não tem Silva')