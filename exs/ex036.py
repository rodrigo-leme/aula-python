"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar.  

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado."""


casa = float(input('Qual o valor da casa? '))
salario = float(input('Digite seu salário atual: '))
anos = int(input('Em quantos anos pretende pagar a casa? '))

prestacao = casa  / (anos * 12)

if prestacao > salario * 0.3:
    print('Empréstimo bancário NEGADO !')
else:
    print('Empréstimo bancário aprovado!! PARABÉNS!')