"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Exemplo: "A sacada da casa", "A torre da derrota"."""


frase = input('Digite uma frase: ').upper().strip()
frase_format = frase.replace(' ', '')

tamanho = len(frase_format)

inverso = ''
for c in range(tamanho-1, -1, -1):
    inverso += frase_format[c]

print(f'O inverso de {frase_format} é {inverso}.')

if inverso == frase_format:
    print('A frase digitada É um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')