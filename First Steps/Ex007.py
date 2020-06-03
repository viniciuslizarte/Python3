# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média.
print('Olá, esse programa calculará a média de duas notas!')
nome = input('Por favor digite seu nome: ')
n1 = int(input('Digite sua primeira nota: '))
n2 = int(input('Digite sua segunda nota: '))
print('{} com base nas suas notas, sua média é {}' .format(nome, (n1 +n2)/2))
