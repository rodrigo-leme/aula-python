"""Escreve um programa que faça o computador "pensar" num número inteiro entre 0 e 5 e peça ao utilizador para tentar 
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o utilizador venceu ou perdeu."""


from random import randint 

n0 = int(input('Descubra o número que eu pensei: '))
# n1 = random.randint(0, 5)
n1 = randint(0, 5)

if n0 == n1:
    print('Parabéns, você acertou !!!')
else:
    print(f'Errou, parceiro(a). Era {n1} \nRode e tente de novo !')

