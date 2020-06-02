'''Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que leie o nome deles e escrevendo o nome do escolhido'''

import random
a1 = input('Primeiro nome: ')
a2 = input('Segundo nome: ')
a3 = input('Terceiro nome: ')
a4 = input('Quarto nome: ')
lista = [a1, a2, a3, a4]
'''Metodo random.choiser - Que escolhe um valor de uma lista'''
s = random.choice(lista)
print('{} você foi o aluno sorteado!' .format(s))
print('FIM PROGRAMA!')


