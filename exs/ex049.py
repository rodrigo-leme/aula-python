"""Refaça o Exercício 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""

t = int(input('Digite um número para tabuada: '))

print(f'A tabuada de {t} é: \n')

for n in range(0, 11):
    print(f'{n}x{t} = {n * t}')