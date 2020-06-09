'''ESCREVA UM PROGRAMA QUE APROVE UM EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA.
O PROGRAMA IRÁ PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE IRÁ PAGAR
CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE ULTRAPASSAR 30% DO SALÁRIO OU ENTÃO O EMPREPÉSTIMO SERÁ NEGADO'''

import time
print('EMPRÉSTIMO BANCÁRIO')
name = str(input('Olá qual é seu nome: ')).upper().strip()
home = float(input('{} qual o valor do imóvel que deseja comprar? R$' .format(name)))
salary = float(input('{} qual é o valor do seu salário? R$' .format(name)))
m = (salary * 30) / 100
year = int(input('{} em quantos anos pretende parcelar este financiamento? ' .format(name)))
print('Ok, estamos analisando seus dados...')
time.sleep(3)
if (home / (year * 12)) > m:
    print('{} infelizmente seu crédito não foi aprovado' .format(name))
else:
    print('PARABÉNS, SEU FINANCIAMENTO FOI APROVADO!!')
    print(('{} o valor da mensalidade ficará R$:{:.2f}') .format(name, (home / (year * 12))))
print('---- FIM ---')

