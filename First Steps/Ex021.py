''' Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome SANTO'''

city = str(input('Digite o nome de uma cidade qualquer: ')).strip()
city1 = city.capitalize()
print('A cidade escolhida começa com Santo?')
print(city1[:5] == 'Santo')
print('FIM!!!')
