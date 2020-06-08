''' Faça um progra que leie um ano qualquer e mostre se este ano é ou não um ano bissexto'''

print('CALCULANDO ANO BISSEXTO!!')
year = int(input('Digite um ano qualquer: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano que de {} é um ano bissexto!' .format(year))
else:
    print('O ano de {} NÃO é um ano bissexto!' .format(year))
print('------ FIM ------')
