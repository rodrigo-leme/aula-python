"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""


ano = int(input('Digite um ano, que vou descobrir se ele é BISSEXTO: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('ANO BISSEXTO PORRAAA')
else:
    print('esse nao é nao, chapa')