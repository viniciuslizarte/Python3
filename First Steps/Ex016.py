'''Faça um programa que leia um ângulo qualquer  e mostre na tela o valor do seno, cosseno e tangente deste ângulo.'''

'''import math
a = float(input('Digite o valor de um ângulo qualquer: '))
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)
print('O seno de {} é {:.3f} \nO cosseno de {} é {:.3f} \nA tangente de {} é {:.3f}' .format(a, s, a, c, a, t))
print('FIM PROGRAMA!')'''

import math
a = float(input('Digite o valor de um ângulo qualquer: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O seno de {} é {:.3f} \nO cosseno de {} é {:.3f} \nA tangente de {} é {:.3f}' .format(a, s, a, c, a, t))
print('FIM PROGRAMA!')