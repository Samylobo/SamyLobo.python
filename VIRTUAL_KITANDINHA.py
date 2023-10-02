''' 
Desafio da Kitandinha virtual 
Faça uma lista de comprar com listas 
O usuario deve ter a possibilidade de inseir ,
  apagar , e listar valores da sua lista 
  Não  permite que o programa quebre com 
  erros de indices inexistentes na lista . 
'''
''''
solução com try/except
 ''' 

lista = []
 
while True:
    entrada = input('[i]nserir [a]pagar [l]istar :')
    if entrada == 'i':
        anotacoes_mercado = input('o que voce quer adicionar na sua lista :')
        lista.insert(0,anotacoes_mercado)
 
    elif entrada == 'a':
        if entrada == 'a':
            anotacoes_mercado = int(input('o que voce quer apagar na sua lista :'))
            try:   
                lista.pop(anotacoes_mercado)
                indices = len(lista)
            except:
                print('esse numeros nao existe')
 
    elif entrada == 'l':
        indices = range(len(lista))
        for indice in indices:
             print(indice,lista[indice])
 
 
    else:
        print('algo deu errado')
