print('Exercício 4 - Concurso cultural entre meninas (até 12 anos) e idosas (maiores de 59 anos)')
print('-----------------------------------------------------------------------------------------')

cont = 0 
while(cont < 10):
    cont = cont + 1
    nome = input('Digite o nome do candidato ' + str(cont) + ': ')
    idade = int(input('Digite a idade do candidato ' + str(cont) + ': '))
    sexo = input('Digite o sexo do candidato ' + str(cont) + ' (M ou F): ')
    
    if (idade <= 12 or idade >= 59) and (sexo == 'F' or sexo == 'f'):
       print('Canditato apto para o concurso') 
    else:   
        print('Candidato não apto para o concurso')

    print('------------------------------------')
