print('Exercicio 3 - Um algoritmo que leia as notas de uma turma de 15 alunos e depois imprima')
print('---------------------------------------------------------------------------------------')

# 1) ler as notas
menor_nota = 0 
maior_nota = 0
soma = 0
cont = 0

while ( cont < 15):
    cont = cont + 1
    nota = float(input('Digite a nota do aluno: '))
    soma = soma + nota

    if(cont == 1 ):
        maior_nota = menor_nota = cont
    
    else: # maior nota
        if( nota > maior_nota ):
            maior_nota = nota

            # menor nota
        if(cont < menor_nota):            
            menor_nota = nota
    
media = soma / cont
print('Maior nota da turma:', maior_nota)

print('Menor nota da turma:', menor_nota)

# média da turma
print('Média de todas as notas:', media)