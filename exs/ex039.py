# """ Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# O seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

nasc = int(input('Digite o seu ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - nasc
# idade = 2026 - nasc


if idade == 18:
    print('I WANT YOU! Você deve se alistar já !')
elif idade > 18:
    print(f'Já passou da época. Reservista há {idade - 18} anos')
elif idade < 18:
    print(f'Ainda faltam {18 - idade } anos para o alistamento')
