'''DESENVOLVA UM PROGRAMA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULANDO O IMC E INFORMANDO NA TELA:
- ABAIXO DO PESO < = 18.5
- PESO IDEAL, DE 18.5 A 25
- SOBREPESO DE 25 A 30
- OBESIDADE 30 A 40
- OBESIDADE MÓRBIDA ACIMA DE 40'''

print('CALCULANDO IMC')
name = str(input('Olá, digite o seu nome: '))
h = float(input('Qual sua altura: '))
p = float(input('Qual seu peso: '))
imc = p / (h ** 2)
if imc <= 18.5:
    print('{} você está abaixo do peso!' .format(name))
elif 18.5 < imc >= 25:
    print("{} parabéns, você está em seu peso ideal!" .format(name))
elif 25 < imc >= 30:
    print('ALERTA!! \n{} você está com sobrepeso!' .format(name))
elif 30 < imc >= 40:
    print('{} você pertence ao grupo de pessoas obesas, procure um médico!' .format(name))
else:
    print('{} cuida da sua, procure um médico! Obsidade mórbida é responsável por inúmeras mortes por ano!' .format(name))
print('---- FIM ----')
