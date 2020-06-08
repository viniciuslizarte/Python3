''' Faça um programa que leia 3 números e mostre na tela qual deles é o maior e qual é o menor'''

print('IDENTIFICANDO NÚMEROS')
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))
menor = n1
maior = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print('O maior número digitado foi {} e o menor número digitado foi {}!' .format(maior, menor))
print('---- FIM ----')