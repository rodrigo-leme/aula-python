"""Desenvolve um programa que pergunte a distância de uma viagem em km.
Calcula o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas."""


dist = int(input('Qual a distância total da viagem em Km? '))

# preco = dist * 0.45 if dist > 200 else dist * 0.5

if dist > 200:
    print(f'O preço da passagem é R${dist * 0.45:.2f}')
else:
    print(f'O preço da passagem é R${dist * 0.5:.2f}')

