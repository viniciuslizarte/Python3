''' Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado
A multa custará R$7 a cada km/h acima do limite'''

print('Analisando velocidade!!')
velo = float(input('Olá, digite a velocidade do seu veículo: '))
velo1 = 80.0
if velo1 >= velo:
    print('Parabéns, você você está dentro das leis de trânsito!!')
else:
    print('VOCÊ ULTRAPASSOU A VELOCIDADE PERMITIDA NA VIA, SUA MULTA FICOU NO VALOR DE R${:. 2f}' .format((velo - velo1)*7))
print('------FIM------')