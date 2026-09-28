"""Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
Exemplo: 
Ana Maria de Souza
Primeiro nome: Ana | Último nome: Souza"""

nome = input('Digite seu nome: ')

dividido = nome.split()

print(f'Primeiro nome: {dividido[0]} | Último nome: {dividido[-1]}')