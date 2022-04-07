print('Exercício 7 - Um programa que calcule todos os números divisíveis por certo valor indicado pelo usuário')
print('-------------------------------------------------------------------------------------------------------')

valor_divisor = int(input('Digite o número divisor: '))

inicio_intervalo = int(input('Digite o intervalo de início: '))

final_intervalo = int(input('Digite o final do intervalo: '))

print('Números divisíveis por', valor_divisor, 'no intervalo de', inicio_intervalo, 'a', final_intervalo, ':')
print('--------------------------------------------')

for n in range (inicio_intervalo, final_intervalo):
 
    if (n % 2) == 0:
        print(n, end = " ")
