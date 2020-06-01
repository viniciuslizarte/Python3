# Faça um programa que leia um número inteiro e mostre na tela seu sucesseor e antecessor.

n = int(input('Olá, por favor digite um número: '))
print('O número digitado foi: {:>3} \nSeu antecessor é: {:>8} \nSeu sucessor é: {:>10}' .format(n, n-1, n+1))
