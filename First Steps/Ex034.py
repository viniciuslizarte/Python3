'''ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO.
1  - PARA BINÁRIO
2 - PARA OCTAGONAL
3 - HEXADECIMAL'''

print('CONVERSÃO DE NÚMEROS!!')
nun = int(input('DIGITE UM NÚMERO: '))
print('''VOCÊ QUE CONVERTER ESSE NÚMERO PARA QUAL BASE?
[1] BINÁRIO
[2] OCTAGONAL
[3] HEXADECIMAL''')
base = int(input('SUA ESCOLHA É: '))
if base == 1:
    print('O NÚMERO {} EM BINÁRIO FICA {}' .format(nun, bin(nun)[2:]))
elif base == 2:
    print('O NÚMERO {} EM OCTAGONAL FICA {}'.format(nun, oct(nun)[2:]))
else:
    print('O NÚMERO {} EM HEXADECIMAL FICA {}' .format(nun, hex(nun)[2:]))
print('---- FIM ----')
