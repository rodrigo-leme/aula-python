larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))

area = larg * alt

print(f'Sua parede tem a dimensão de {larg}x{alt}m² e sua área é de {area}m²')
print(f'Será necessário utilizar {area / 2:.1f}l de tinta')
