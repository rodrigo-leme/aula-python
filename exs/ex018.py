from math import radians, sin, cos, tan

angulo = float(input('Digite o Ângulo desejado: '))

seno = sin(radians(angulo))
print(f'O Seno de {angulo} é {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O Cosseno de {angulo} é {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'A Tangente de {angulo} é {tangente:.2f}')