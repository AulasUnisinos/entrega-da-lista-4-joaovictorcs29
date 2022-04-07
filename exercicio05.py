import random

print('Exercício 5 - Um programa que sorteia um número de 1 a 10 e dá ao usuário 3 tentativas de acertá-lo')
print('---------------------------------------------------------------------------------------------------')

#Sortear um numero de 1 a 10
sorteio = random.randint (1, 10)
cont = 0 

while ( cont < 3 ):
    tentativa = int(input('Tente acertar o número (1 a 10): ')) 
    cont = cont + 1
    
    if tentativa < 1 or tentativa > 10:
        print('Número não aceito')   
    elif sorteio > tentativa:
       print('O número está acima')
    elif sorteio < tentativa:
       print('O número está abaixo')   
    elif sorteio == tentativa:
        print('Você acertou o número era', sorteio)
        exit()
    print('-----------------------')
else: 
    print('Não acertou o número sorteado o número era:', sorteio)
