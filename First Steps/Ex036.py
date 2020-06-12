'''FAÇA UM PROGRAMA QUE LEIA A DATA DE NASCIMENTO DE UM JOVEM E INFORME DE ACORDO COM SUA IDADE:
- AINDA DEVERÁ ALISTAR AO SERVIÇO MILITAR
- SE JÁ É A HORA DE SE ALISTAR
- SE JÁ PASSOU O TEMPO DE ALISTAMENTO
O PROGRAM TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE JÁ PASSOU PARA O ALISTAMENTO'''

print('CALCULANDO ALISTAMENTO!')
name = str(input('Olá, qual seu nome '))
na = int(input('Em qual ano você nasceu? '))
if  na > 2002:
    print('{} você deverá se alistar em {} anos!' .format(name, na - 2002))
elif na < 2002:
    print('{} você se alistou há {} anos!' .format(name, 2002 - na))
else:
    print('{} você deverá se alistar este ano!' .format(name))
print('--- FIM ---')

