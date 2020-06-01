# Faça um algoritmo que leia o salário e mostre seu novo salário com 15% de aumento.

print('CALCULANDO AUMENTO SALARIAL! \n')
s = float(input('Digite do valor do seu salário atual: '))
a = ((15*s)/100)
print('Seu salário atual é de R$ {:.2f} \nVocê recebeu um aumento de R$ {:.2f} \nSeu novo salário é R$ {:.2f}' .format(s, a, (s+a)))
print('\nOBRIGADO!')


