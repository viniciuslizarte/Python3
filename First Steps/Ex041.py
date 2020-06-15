'''ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO
- A VISTA 10% OFF EM DINHEIRO OU CHEQUE
- A VISTA 5% OFF CARTÃO
- ATÉ 2X PREÇO NORMAL
- 20% DE JURO ACIMA DE 2X '''''


print('CALCULANDO PAGAMENTO')
v = float(input('Olá qual o valor do produto? R$ '))
p = int(input('Qual será a forma de pagamento? Digite 1 para Dinheiro, 2 para Cartão e 3 para Cheque '))
d1 = (v * 10) / 100
d2 = (v * 5) / 100
j = (v * 20) / 100

if p == 1 or p == 3:
    print('Seu produto possui um desconto de R${}\nO valor final é de R${} ' .format(d1, v - d1))
else:
    print('OK, SUA FORMA DE PAGAMENTO SERÁ CARTÃO!')
    q = int(input('Em quantas vezes você irá pagar o produto? '))
    if q == 1:
        print('Seu produto possui um desconto de R${}\nO valor final é de R${}' .format(d2, v - d2))
    elif q == 2:
        print('O valor do produto é de R${} e será pago em 2X de R${}' .format(v, v / 2))
    else:
        print('Para parcelamentos maior acima de 2X incorre em juro de 20%\nVocê pagará {} parcelas de R${}' .format(q, (v + j) / q))
print('---- FIM ----')