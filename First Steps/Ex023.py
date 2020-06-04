''' Faca um programa que leia uma frase e mostre:
1 - Quantas vezes aparece a letra A
2 - Em que posição ela aparece pela primeira vez
3 - Em que posição ela aparece pela última vez'''

frase = str(input('Digite uma frase qualquer: ')).strip()
frase1 = frase.lower()
print('A frase digitada foi:\n{}' .format(frase))
print('A letra A aparece {} vezes na frase\nA primeira vez em que o A aparece é na posição {}\nA última vez em que aparece é na posição {}.' .format(frase1.count('a'), frase.find('a'), frase1.rfind('a')))
print('FIM!!!')
