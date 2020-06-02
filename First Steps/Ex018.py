'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos trabalhos de seus alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

import random
a1 = input('Digite o primeiro nome: ')
a2 = input('Digite o segundo nome: ')
a3 = input('Digite o terceiro nome: ')
a4 = input('Digite o quarto nome: ')
lista = [a1, a2, a3, a4]
# Função suffle server pra embaralhar!
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
print('FIM PROGRAMA!!')

