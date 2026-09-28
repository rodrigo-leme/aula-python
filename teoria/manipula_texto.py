frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[::2])
print(frase[1::2])

print(frase.count('0'))
print(frase.upper().count('0'))
print(frase.strip())
print(frase.replace('Python', 'Android'))

print('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('curso'))

print(frase.split())
frase3 = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])

print(len(frase))

frase2 = 'Curso em Vídeo Python'
frase2 = frase2.replace('Python', 'Android')
print(frase2)


