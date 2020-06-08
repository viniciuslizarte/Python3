''' Escreva um programa que faça o computador pensar em um número inteiro de 0 a 5 e peça para o usuário descobrir qual foi o número escolhido
pelo computador O computador deverá escrever na tela se o usuário Venceu ou perdeu.'''

import random
nun = random.randint(0, 5)
print('Acerte o Número!')
nun1 = int(input('Digite um número inteiro de 0 a 5: '))
print('Analisando o resultado...')
if  nun == nun1:
    print('Parabéns você acertou em cheio!!!!')
else:
    print('Não foi dessa vez, o número correto era: {}' .format(nun))
print('------FIM------')
