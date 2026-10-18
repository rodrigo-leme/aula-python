""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

À vista dinheiro/PIX: 10% de desconto

À vista no cartão: 5% de desconto

Em até 2x no cartão: preço formal

3x ou mais no cartão: 20% de juros"""


valor = float(input('Digite o valor do produto: R$'))

print(""" 
Opções de Pagamento:
1 - À vista
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão
""")

pagamento = int(input('Escolha um número referente à condição de pagamento pretendida: '))

if pagamento == 1:
    print(f'10% de desconto, valor final será de R${valor - (valor * 0.1):.2f}')
elif pagamento == 2:
    print(f'5% de desconto, valor final será de R${valor - (valor * 0.05):.2f}')
elif pagamento == 3:
    print(f'preço formal, 2 parcelas de R${valor / 2:.2f}')
elif pagamento == 4:
    print(f'20% de juros, preço final será de R${valor + (valor * 0.2):.2f}')
else:
    print('Opção Inválida!!! Escolha uma opção de 1 a 4')