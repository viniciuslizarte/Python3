''' Desenvolva um programa  que pergunte a distância da viagem em km.
1 - Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km
2 - Calcule o preço da passagem cobrando R$0,45 por km para viagens acima de 200km'''

print('VALOR DA PASSAGEM')
travel = float(input('Digite qual a distância em km será percorrida nesta viagem: '))
if travel <= 200:
    print('O valor da sua passagem ficou R${}' .format(travel * 0.5))
else:
    print('O valor da sua passagem ficou R${}' .format(travel * 0.45))
print('------ FIM ------')


#racesystem-stg.cgzshounia8v.us-east-1.rds.amazonaws.com
#am%Y$0x0