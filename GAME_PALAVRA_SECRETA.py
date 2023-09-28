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
   
