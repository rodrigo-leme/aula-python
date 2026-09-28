""" Crie um programa que:

Importe o módulo necessário.
Gere um número aleatório entre 1 e 10.
Exiba esse número na tela.

Exemplo de saída:

Número sorteado: 7

Ao invés de apenas mostrar o número, peça para o usuário tentar adivinhar:

Digite um número entre 1 e 10: 4
Você acertou!"""

import random

n1 = int(input('Adivinhe um número de 1 a 14: '))

numero_sorteado = random.randint(1, 14)

if n1 == numero_sorteado:
    print('PARABÉNS! VOCÊ ACERTOU !!')
else:
    print(f'Que pena, era {numero_sorteado} tente novamente')