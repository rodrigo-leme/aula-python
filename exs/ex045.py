""" Crie um programa que faça o computador jogar Jokenpô (Pedra, Papel e Tesoura) com você."""


# from random import randint

# print('Jokenpô')

# print("""Suas opções:
# [0] PEDRA
# [1] PAPEL
# [2] TESOURA
# """)

# itens = ('Pedra', 'Papel', 'Tesoura')
# player = int(input('Digite sua jogada: '))
# compute = randint(0, 2)

# print("""
# JO
# KEN
# PO!!!\n"""
# )

# print('-='*10)
# # print(f'Jogador jogou {itens[player]} e Computador jogou {itens[compute]}')
# if 0 <= player <= 2: print(f'Jogador jogou {itens[player]} e Computador jogou {itens[compute]}')
# print('-='*10)

# if player == compute:
#     print('EMPATE! Rode de novo.')
# elif player == 0 and compute == 1:
#     print('Computador ganhou')
# elif player == 0 and compute == 2:
#     print('Jogador ganhou')
# elif player == 1 and compute == 0:
#     print('Jogador ganhou')
# elif player == 1 and compute == 2:
#     print('Computador ganhou')
# elif player == 2 and compute == 0:
#     print('Computador ganhou')
# elif player == 2 and compute == 1:
#     print('Jogador ganhou')
# else:
#     print('Aí não, pô! Número inválido. Tenta de novo, um número entre 0 e 2')



from random import randint

print('Jokenpô')

print("""Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
""")

itens = ('Pedra', 'Papel', 'Tesoura')
player = int(input('Digite sua jogada: '))

if player not in (0, 1, 2):
    print('Aí não, pô! Número inválido. Tenta de novo, um número entre 0 e 2')
else:
    compute = randint(0, 2)

    print("""
JO
KEN
PO!!!\n""")

    print('-='*10)
    print(f'Jogador jogou {itens[player]} e Computador jogou {itens[compute]}')
    print('-='*10)

    if player == compute:
        print('EMPATE! Rode de novo.')
    elif (player == 0 and compute == 2) or (player == 1 and compute == 0) or (player == 2 and compute == 1):
        print('Jogador ganhou')
    else:
        print('Computador ganhou')