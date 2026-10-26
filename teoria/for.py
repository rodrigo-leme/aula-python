# for c in range(1, 10):
#     passo
# pega


for c in range(0, 6):
    print('oi')
print('FIM')


for c in range(1, 7):
    print(c)
print('FIM')


for c in range(6, 0, -1):
    print(c)
print('FIM')


for c in range(0, 7, 2):
    print(c)
print('FIM')



n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')



i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')



s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n  # s = s + n
print(s)
print('fim')
