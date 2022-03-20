print('_____________________________________________')
print('Bem vindo ao jogo de advinhação ')
print('_____________________________________________')

numero_secreto = 42
totativa = 3
rodada = 1

while(rodada <= totativa):
    print('Tentativas', rodada,'de', totativa)
    chute_str = input('Digite seu numero ')
    print('Você digitou', chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute  > numero_secreto   
    menor   = chute  < numero_secreto

    if(acertou):
        print('Você acertou')
    else:
        if(maior):
            print('Você errou! O seu chute foi maior ')
        elif(menor):
            print('Você errou! O seu chute foi menor ')

    rodada = rodada + 1
    print('Fim do jogo')