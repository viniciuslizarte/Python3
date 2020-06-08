'''Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou IMPAR'''

print('PAR OU ÍMPAR!')
nun = float(input('Digite um número qualquer: '))
p = (nun % 2)

if p == 0:
    print('O numero digitado foi {} e ele é um número PAR!' .format(nun))
else:
    print('O número digitado foi {} e ele é um número ÍMPAR!' .format(nun))
print('------FIM------')