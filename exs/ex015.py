# km_run = float(input('Digite quantos Km rodados: '))
# day_use = int(input('Dias alugados: ')) 

# rent = day_use * 60

# price = rent + (km_run * 0.15)

# print(f'Preço total a pagar: R${price}')




# km_run = float(input('Digite quantos Km rodados: '))
# day_use = int(input('Dias alugados: ')) 

# print(f'Preço total a pagar: R${day_use * 60 + (km_run * 0.15)}')




km_run = float(input('Digite quantos Km rodados: '))
day_use = int(input('Dias alugados: '))

price = day_use * 60 + km_run * 0.15

print(f'Preço total a pagar: R${price}')


""" Existe até uma regra prática bastante usada em engenharia de software: não sacrifique a clareza do código para economizar uma operação extremamente barata, a menos que você tenha medido e comprovado que aquilo é um gargalo."""