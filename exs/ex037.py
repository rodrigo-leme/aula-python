"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:  

1 para Binário

2 para Octal

3 para Hexadecimal"""


numero = int(input('Digite um número inteiro: '))

opcao = int(input("""\nEscolha uma das bases para conversão 
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL
\nOpção escolhida: """))


if opcao == 1:
    print(f'{numero} convertido para BINARIO é igual a {bin(numero) [2:]}')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero) [2:]}')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero) [2:]}')
else:
    print('Opção inválida! Escolha um número de 1 a 3')