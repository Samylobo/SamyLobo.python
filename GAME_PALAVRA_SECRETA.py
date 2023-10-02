''' DESAFIO 
Faça um jogo para o usuário adivinha qual 
a palavra secreta. 
Você vai propor uma palavra secreta qualquer 
e vai dar a possibilidade para o usuário digitar uma letra.
Quando o usuário digitar uma letra, você vai conferir se a
 letra digitada está na palavra secreta.
    SE A PALAVRA DIGITADA ESTIVER NA PALAVRA SECRETA;
    EXIBA A LETRA
    SE A LETRA DIGITADA NÃO ESTIVER NA PALAVRA SECRETA;
    EXIBA *.
    FAÇA A CONTAGEM DE TENTATIVAS DO SEU USUÁRIO.
'''
palavra_secreta = 'bruxa'
letras_acertadas = ''
qtd_tentativas = 0
while True:
    letra_d = input ('Digite uma letra: ')
    qtd_tentativas +=1 

    if len(letra_d) >1:
        print('Digite apenas uma letra. ')
        continue

    if letra_d in palavra_secreta:
       letras_acertadas += letra_d
    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += (letra_secreta)
        else:
            palavra_formada +='*'  
    print('palavra formada: ',palavra_formada)

    if palavra_formada == palavra_secreta:
        print(' VOCÊ GANHOU, PARABÉNS!')
        print('A palavra era', palavra_formada)
        print('Tentativas: ', qtd_tentativas)
        break
  ''' 
    Utilizei 3 perfil para teste
  1 jovem 
  2 meia idade 
  3 mais idade 
  
  o número 3 teve mais dificuldades de descobri sobre o que era , sem saber uma dica , 
após a dica 'jogo da forca , foi se inicando uma interação melhor mais ainda com dificuldades 
 tentativas : 18.'''

'''o numero 1, não teve dificuldades para entender o jogo , e muita dificuldade com a acertividade de tentativas 
tentativas : 34.'''

'''o numero 2 , não teve dificuldade para entender o jogo e , usou de estrategias para facilitar a acertividade 
tentativas : 11 .'''
  
''' O Objetivo foi a comprensão do while e a forma mais pratica do if/ elif/else/ continue/ break    '''
