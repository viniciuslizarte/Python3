# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# calcule e mostre o comprimento da hipotenusa.

import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(ca, co)
print('A soma dos catetos digitado resultam em uma hipotenusa igua a {:.2f}' .format(hi))
print('FIM PROGRAMA!')