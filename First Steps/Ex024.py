''' Faça um programa que leia o nome completo de uma pessoa, mostrando separadamente o primeiro e o último nome
EX - ANA MARIA SILVA primeiro=ANA e último= SILVA'''

name = str(input('Digite seu nome completo: ')).strip().upper()
name1 = name.split()
print('O nome que digitou foi \n{}' .format(name))
print('O primeiro nome é: {}\nO último nome é: {}' .format(name1[0], name1[len(name1)-1]))
print('FIM!!!')
