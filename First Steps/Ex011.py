# Faça um programa que leia a altura e a largura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la
# Considere que 1L de tinta pinta uma área de 2m.

print('CALCULANDO A QUANTIDADE DE TINTA NECESSÁRIA!\n')
a = int(input('Qual a antura da parede que irá pintar? '))
l = int(input('Qual a largura da parede que irá pintar'))
t = int(2)
print('Para uma parde de {} metros de altura e {} metros de largura é necessário {} litros de tinta.' .format(a, l, ((a*l)/t)))
print('OBRIGADO!')