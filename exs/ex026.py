"""Faça um programa que leia uma frase pelo teclado e mostre:  
Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.  """

# strip remove espaço das pontas
frase = input('Digite uma frase: ').upper().strip()



print(f'a letra a aparece {frase.count("A")} vezes na frase')
print(f'a primeira letra a aparece na posição {frase.find("A")}')
print(f'a ultima letra a aparece na posição {frase.rfind("A")}')
