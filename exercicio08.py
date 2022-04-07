print('Exercício 8 - Para X alunos da Unisinos, ler as notas do grau A e grau B e calcular a média considerando o sistema de notas da Unisinos')
print('---------------------------------------------------------------------------------------------------------------------------------------')

cont = 1
media_geral = 0
opcao = 's'

while opcao != 'n':

    aluno = input('Digite o nome do aluno ' + str(cont) + ': ')
    notaA = float(input('Digite a nota do grau A: '))
    notaB = float(input('Digite a nota do grau B: '))
    media = (notaA + notaB) / 2
    
    if media >= 6:
        print('------------------------')
        print('APROVADO')
        print('------------------------')
    else:
        print('----------------------------')
        print('Aluno ' + aluno + ' em recuperação')
        print('----------------------------')

        notaC = float(input('Digite a nota do grau C: '))
        grau_substituido = input('Qual grau substituir pelo grau C? (A ou B): ')

        if grau_substituido == 'A' or grau_substituido == 'a':
            media = (notaC + notaB) / 2
        elif grau_substituido == 'B' or grau_substituido == 'b':
            media = (notaA + notaC) / 2
        
            if media >= 6:
                print('------------------------')
                print('APROVADO')
                print('------------------------')
            else:
                print('------------------------')
                print('REPROVADO')
                print('------------------------')

    media_geral = media_geral + media / 2
    opcao = input('Deseja informar outro aluno? (s/n) ') or 's'
    cont = cont + 1

print('------------------------')
print('A média geral dos alunos foi de', media_geral)
