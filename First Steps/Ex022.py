''' Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome'''

name = str(input('Digite seu nome completo: ')).strip()
name1 = name.upper()
print('O nome digitado foi {}' .format(name1))
print('SILVA' in name1)
print('FIM!!!')
