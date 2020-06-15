'''CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ'''

print('VAMOS JOGAR JOKENPÔ!!\n')
import random, time
c = ['PEDRA', 'PAPEL', 'TESOURA']
vc = int(input('Escolha 1 para PEDRA, 2 para PAPEL e 3 para TESOURA '))
c1 =random.choice(c)
print(' COMPUTADOR ESCOLHEU {}\n' .format(c1))
print('ANALISANDO RESULTADO...\n')
time.sleep(1)
if vc == 1 and c1 == 'PEDRA':
    print('JOGO EMPATADO!!')
elif vc == 1 and c1 == 'PAPEL':
    print('VOCÊ PERDEU!!')
elif vc == 1 and c1 == 'TESOURA':
    print('VOCÊ GANHOU!!')
elif vc == 2 and c1 == 'PEDRA':
    print('VOCÊ GANHOU!!')
elif vc == 2 and c1 == 'PAPEL':
    print('JOGO EMPATADO!!')
elif vc == 2 and c1 == 'TESOURA':
    print('VOCÊ PERDEU!!')
elif vc == 3 and c1 == 'PEDRA':
    print('VOCÊ PERDEU!!')
elif vc == 3 and c1 == 'PAPEL':
    print('VOCÊ GANHOU!!')
else:
    print('JOGO EMPATADO!!')
print('--- FIM ---')
