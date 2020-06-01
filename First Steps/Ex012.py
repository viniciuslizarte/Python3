# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

print('CALCULANDO DESCONTE DE PRODUTO! \n')
p =float(input('Digite o valor do produto: '))
np = ((5*p)/100)
print('O valor do produto é R$ {:.2f}, mas com o desconto promocional de 5% o valor fica R$ {:.2f}' .format(p, (p-np)))
print('OBRIGADO!')
