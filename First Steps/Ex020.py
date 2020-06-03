''' Faça um programa que leia um número de 0 a 9999 e mostre na tela um dos dígitos separados
Ex: 1834 unidade 4, dezena 3, centena 8 e milhar 1'''

nun = str(input('Digite um número inteiro entre 0 a 9999: '))
print('Milhar = {}\nCentena = {}\nDezena = {}\nUnidade = {}' .format(nun[0], nun[1], nun[2], nun[3]))
print('FIM!!!')
