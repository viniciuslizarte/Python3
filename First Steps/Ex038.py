'''A CONFEDERAÇAO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA A DATA DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA DE ACORDO COM SUA IDADE:
- MIRIM ATÉ 9 ANOS
- INFANTIL ATÉ 14 ANOS
- JUNIOR ATÉ 19 ANOS
- SENIOR ATÉ 20 ANOS
- MASTER ACIMA DE 20'''

print('CALCULANDO CATEGORIA')
name = str(input('Olá digite seu nome: '))
na = int(input('Em que ano você nasceu? '))
age = 2020 - na
if age <= 14:
    print('{} Você pertence a categoria INFANTIL!' .format(name))
elif 14 < age <= 19:
    print('{} você pertence a categoria JUNIOR!' .format(name))
elif age == 20:
    print('{} você pertence a categoria SÊNIOR!' .format(name))
else:
    print('{} você já é um atleta MASTER!' .format(name))
print('---- FIM ----')
