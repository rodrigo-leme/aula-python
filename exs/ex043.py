""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre o seu status, de acordo com a tabela abaixo:

Abaixo de 18.5: Abaixo do Peso

Entre 18.5 e 25: Peso Ideal

25 até 30: Sobrepeso

30 até 40: Obesidade

Acima de 40: Obesidade Mórbida"""


peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do Peso')
elif 18.6 < imc < 25:
    print('Peso Ideal')
elif 26 < imc < 30:
    print('Sobrepeso')
elif 31 < imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
