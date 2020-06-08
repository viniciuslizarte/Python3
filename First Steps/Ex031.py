''' Escreva um programa que leia o valor do salário de uma pessoa e calcule o valor do salário com um aumento:
1 - Para salários abaixo de R$2000,00 aumento de 15%
2 - Para salários acima de R$2000,00 aumento de 10%'''

print('AUMENTO SALARIAL')
salario = float(input('Digite o valor do seu salário: R$'))
a = (salario * 15) / 100
b = (salario * 10) / 100
if salario <= 2000:
    print('Seu aumento foi de R${:.2f}\nSeu novo salário é R${:.2f}'.format(a, salario + a))
else:
    print('Seu aumento foi de R${:.2f}\nSeu novo salário é R${:.2f}' .format(b, salario + b))
print('---- FIM ----')