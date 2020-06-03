''' Crie um progragam que leia o nome completo de uma pessoa e mostre:
1 - O nome com todas as letras maiúsculas
2 - O nome com todas as letras minúscuslas
3  - Quantas letras tem sem considerar os espaços
4 - Quantas etras tem o primeiro nome'''

nome = str(input('Digite seu nome completo: '))
print('Seu nome completo é: {}\nEm letras maiúsculas fica: {}\nEm letras minúsculas fica: {}' .format(nome, nome.upper(), nome.lower()))
# Função len() conta quantos caracteres tem ao todo e a função .count eu posso escolher oque vai contar
print('Sem contar os espaços, {} possui {} caracteres.' .format(nome, len(nome) -nome.count(' ')))
# Função find encontra a posição que quer encontrar... nesse casa procurei o primeiro espaço que é a separação dos nomes
print('Seu primeiro nome possui {} caracteres!' .format(nome.find(' ')))
print('FIM PROGRAMA!!!')
