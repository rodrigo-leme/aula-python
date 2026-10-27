# """Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade (21 anos) e quantas já são maiores."""

from datetime import date

cont = 0
ano_atu = date.today().year
total = 7
for c in range(total):
    ano_nasc = int(input('Digite o ano de nascimento: '))
    maioridade = ano_atu - ano_nasc
    if maioridade >= 21:
        cont += 1

print(f'\nNúmero de pessoas com maioridade: {cont}\nNúmero com menoridade: {total - cont}')

