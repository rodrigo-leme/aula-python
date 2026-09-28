"""Escreve um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80 km/h, mostra uma mensagem a dizer que foi multado. 
A multa vai custar R$ 7,00 por cada km acima do limite."""

velo = int(input('Qual a velocidade atual do carro? '))

multa = (velo - 80) * 7

if velo > 80:
    print(f'Você foi multado em R${multa:.2f} ! \nVelocidade limite ultrapassada!')
else:
    print('Sem problemas! Você está dentro do limite.')