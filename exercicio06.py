print('Exercício 6 - Um programa que lê um número de 1 a 9 e mostra a produto de multiplicação do número')
print('-------------------------------------------------------------------------------------------------')

opcao = 's'
while opcao != 'n':
    cont = 1
    numero_escolhido = int(input('Digite um número de 1 a 9: '))
    if numero_escolhido > 0 and numero_escolhido < 11:
        print('----------------------------')
        print('Tabuada do número', numero_escolhido)
        while (cont < 10):
            produto = numero_escolhido * cont
            print(numero_escolhido, 'x' , cont, '=', produto)
            cont = cont + 1
        print('----------------------------')
        opcao = input('Deseja informar outro número? (s/n) ') or 's'
    else:
        print('Número inválido')
