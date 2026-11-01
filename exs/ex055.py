"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

total_people = 5
compare = []

for _ in range(total_people):
    weight = float(input('Digite o peso: '))
    compare.append(weight)
    

print(f'O maior peso informado é {max(compare)} e o menor é {min(compare)}')


