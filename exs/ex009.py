n1 = int(input('Digite um número: '))

print(f'\nA tabuada de {n1} é:')
for x in range(1, 11):
    # tabuada = n1 * x
    # print(f'tabuada = {tabuada}')
    print(f' {n1} x {x} = {n1 * x}')
