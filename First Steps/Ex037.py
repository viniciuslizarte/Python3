''' CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCUE SUA MÉDIA, MOSTRANDO NO FINAL UMA MENSAGEM DE ACORDO COM A MÉDIA ATINGIDA:
- MÉDIA ABAIXO DE 5, REPROVADO
- MÉDIA ENTRE 5 E 6.9, RECUPERAÇÃO
- MÉDIA IGUAL OU SUPERIOR A 7, APROVADO'''

print('CALCULANDO MÉDIAS')
a = float(input('Olá digite sua primeira nota: '))
b = float(input('Digite sua segunda nota: '))
m = (a + b) / 2
print('Analisando sua situação...')
import time
time.sleep(2)
if m >= 7:
    print('VOCÊ FOI APROVADO!!\nSUA MÉDIA FOI {}' .format(m))
elif m < 5:
    print('VISH, VOCÊ FOI REPROVADO =/\n SUA MËDIA FOI {}' .format(m))
else:
    print('UUH FOI QUASE, VOCÊ ESTA DE RECUPERAÇÃO!\n SUA MÉDIA ESTA EM {}' .format(m))
print('--- FIM ----')
