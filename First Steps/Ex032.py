'''''Desenvolva um programa que leia 3 comprimentos de retas e imprima se ele pode ou não formar um triângulo'''

print('PODE OU NÃO SER UM TRIÂNGULO...')
r1 = float(input('Digite o valor de uma reta: '))
r2 = float(input('Digite o valor de uma reta: '))
r3 = float(input('Digite o valor de uma reta: '))
r4 = (r1 + r2)
r5 = (r2 + r3)
r6 = (r1 + r3)
if r1 < r5 and r2 < r6 and r3 < r4:
    print('Com as medidas informadas é possível construir um Triângulo!')
else:
    print('Com as medidas informadas NÃO é possível forma um triângulo.')
print('---- FIM ----')
