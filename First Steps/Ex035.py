'''ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E OS COMPARE, MOSTRANDO NA TELA  UMA MENSAGEM:
1 - O PRIMEIRO VALOR É O MAIOR
2 - O SEGUNDO VALOR É O MAIOR
3 - NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS'''

print('IDENTIFICANDO NÚMEROS')
a = int(input('Olá digite um númeiro inteiro: '))
b = int(input('Digite digite mais um número inteiro: '))
if a > b:
    print('O maior número é: {}\nO menor número é: {}' .format(a, b))
elif b > a:
    print('O mairo número é: {}\nO menor número é: {}' .format(b, a))
else:
    print('Os dois números digitados são iguais!')
print('---- FIM ----')
