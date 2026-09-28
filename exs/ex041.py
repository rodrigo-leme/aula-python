""" A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a categ:  

Até 9 anos: MIRIM  

Até 14 anos: INFANTIL  

Até 19 anos: JÚNIOR  

Até 25 anos: SÊNIOR

Acima de 25 anos: MASTER"""

from datetime import date

nasc = int(input('Digite seu ano de nascimento: '))
categ = date.today().year - nasc

if categ <= 9:
    print('Categoria MIRIM')
elif categ <= 14:
    print('Categoria INFANTIL')
elif categ <= 19:
    print('Categoria JÚNIOR')
elif categ <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')