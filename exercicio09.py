
print('Exercicio 9 - Um programa que leia o nome de pessoas e a sua profissão')
print('----------------------------------------------------------------------')

#1) Ler o nome e sua profissão
cont = 0

while True:
    nome = input('Nome: ')
    if nome == 'fim':
        print('O número de advogadas ou advogados cadastrados é', cont)
    if nome != 'Fim':
       profissão = input('Profissão: ')
    if profissão == 'advogado' or 'advogada':
       cont = cont + 1
        
 