"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""


# n = int(input('Digite um número: '))
# cont = 0
# for c in range(1, n+1):
#     if n % c == 0:
#         cont += 1

# if cont == 2:
#     print('primo')
# else:
#     print('não primo')


# -------------------------------------------------------------


# n = int(input('Digite um número: '))
# cont = 0
# for c in range(1, n+1):
#     if n % c == 0:
#         cont += 1
#         if cont > 2:
#             break

# if cont == 2:
#     print('primo')
# else:
#     print('não primo')



n = int(input('Digite um número: '))
primo = True

if n < 2:
    primo = False

for c in range(2, int(n ** 0.5) + 1):
    if n % c == 0:
        primo = False
        break

if primo:
    print('primo')
else:
    print('não primo')



# testes velocidade
# 859
# 1000003
# 100000007
