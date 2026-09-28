n1 = float(input('Digite o valor em metros: '))

cm = n1 * 100
mm = n1 * 1000

# print(f'O valor de {n1}m em centímetros é de {cm:.2f} e em milímetros é de {mm:.2f}')

# if n1 == type(int):
#     print(f'O valor de {n1:.1f}m em centímetros é de {cm:.2f}cm e em milímetros é de {mm:.2f}mm')
# else:
#     print(f'O valor de {n1:.2f}m em centímetros é de {cm:.2f}cm e em milímetros é de {mm:.2f}mm')


if n1.is_integer():
    print(f'O valor de {n1:.0f}m em centímetros é de {cm:.0f}cm e em milímetros é de {mm:.0f}mm')
else:
    print(f'O valor de {n1:.1f}m em centímetros é de {cm:.0f}cm e em milímetros é de {mm:.0f}mm')