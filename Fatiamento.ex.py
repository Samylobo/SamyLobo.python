''' Nesse exercicio , eu mostro meus conhecimentos básico como o Fatiamnto de string [i:f:p][::] e a função len que retorna a quantidade de caracteres da string. '''


nome = input ("Digite o seu nome:")
idade = input('Digite sua idade:')

if nome and idade:
        print(f'Seu nome é {nome}')
        print(f'Seu nome invertido é {nome[::-1]}')
 
        if ' ' in nome:
               print('Seu nome contém  espaços.')
        else:
               print('Seu nome NÃO cotém espaços.')  

               print(f'Seu nome tem {len(nome)} letras.')
               print(f'A primeira letra do seu nome é {nome[0]}.')
               print(f'A última letra do seu nome é {nome[-1]}.')
else:
               print("Desculpe , você deixou campos vazios.")

 
