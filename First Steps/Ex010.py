# Escreva um programa que leia quanto de dinheiro ela tenha na carteira e mostre quantos Dólares ela pode comprar.
# Considere U$D 1.00 = R$ 4,81

print('PROGRAMA CONVERSÃO DE MOEDAS!\n')
r = float(input('Olá qual a sua quantia em R$? '))
d = 4.81
print('Com R$ {:.2f} é possível comprar U$D {:.2f}' .format(r, r/d))
print('\nOBRIGADO!')