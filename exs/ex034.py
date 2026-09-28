"""Escreve um programa que pergunte o salário de um funcionário e calcula o valor do seu aumento. 
Para salários superiores a R$ 1.250,00, calcula um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""


sal = float(input('Digite seu salário atual: '))

if sal > 1250:
    novo_salario = (sal * 0.1) + sal
    print(f'Você terá um aumento de: R${novo_salario:.2f}')
else:
    novo_salario = (sal * 0.15) + sal 
    print(f'Você terá um aumento de: R${novo_salario:.2f}')