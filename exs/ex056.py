"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:   
1. A média de idade do grupo.
2. Qual é o nome do homem mais velho.
3. Quantas mulheres têm menos de 20 anos."""



total = 5
list1 = []

old_men = 0 
old_name = ''

woman20 = 0

for c in range(total):
    name = input('Digite seu nome: ')
    age = int(input('Digite sua idade: '))
    sex = input('Sexo [M/F]: ').upper()
    
    list1.append(age)

    print('-'*22)

    if c == 1 and sex == 'M':
        old_men = age
        old_name = name
    if sex == 'M' and age > old_men:
        old_men = age
        old_name = name
    if sex == 'F' and age < 20:
        woman20 += 1


print(f'A média de idade do grupo é {sum(list1) / total:.0f}')
print(f'O nome do homem mais velho é {old_name}')
print(f'O total de mulheres com menos de 20 anos é {woman20}')
