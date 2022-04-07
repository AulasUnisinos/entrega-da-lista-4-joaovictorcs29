print('Exercício 10 - Uma lista de cinco nomes informados pelo usuário, qual o primeiro em ordem alfabética')
print('----------------------------------------------------------------------------------------------------')

primeiro_nome = input('Digite o nome: ')
for n in range (1, 5):
    nome = input('Digite o nome: ')
    if(primeiro_nome > nome):
        primeiro_nome = primeiro_nome = nome
print('Primeiro nome em ordem alfabética:', primeiro_nome)
