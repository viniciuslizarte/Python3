'''CRIA UM PROGRAMA QUE LEIA O COMPRIMENTO DE 3 RETAS E VEJA SE É POSSÍVEL FORMAR UM TRIÂNGULO
SE SIM, MOSTRE QUAL É O TIPO DE TRIÂNGULO FORMADO
- EQUILÁTERO, TODOS OS LADOS IGUAIS
- ISÓSCELES, DOIS LADOS IGUAIS
- ESCALENO, TODOS OS LADOS DIFERENTES'''

print('IDENTIFICANDO TRIÂNGULOS')
a = float(input('DIGITE UM COMPRIMENTO DE UM RETA: '))
b = float(input('DIGITE UM COMPRIMENTO DE UMA RETA: '))
c = float(input('DIGITE UM COMPRIMENTO DE UM RETA: '))
if (a + b) < c or (a + c) < b or (b + c) < a:
    print('COM OS VALORES DO INFORMADOS, NÃO É POSSÍVEL FORMAR UM TRIÂNGULO!!')
elif (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
    print('ESTE TRIÂNGULO É UM TRIÂNGULO ISÓSCELES! ' )
elif (a == b and b == c) or (b == c and c == a):
    print('ESTE TRIÂNGULO É UM TRIÂNGULO EQUILÁTERO!')
else:
    print('ESTE TRIÂNGULO É UM TRIÂNGULO ESCALENO!')
print('---- FIM ----')