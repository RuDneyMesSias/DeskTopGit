print('_____________________________________________')
print('Bem vindo ao jogo de advinhação ')
print('_____________________________________________')

numero_secreto = 42
totativa = 3

for rodada in range(1, totativa +1):
    print('Tentativa {} de {}'.format(rodada, totativa))
    chute_str = input('Digite seu número ')
    print('Você digitou', chute_str)
    chute = int(chute_str)

    if(chute <1 or chute > 100):
        print('Você deve digitar um número entre 1 e 100!')
        continue

    acertou = chute == numero_secreto
    maior   = chute  > numero_secreto   
    menor   = chute  < numero_secreto

    if(acertou):
        print('Você acertou')
        break
    else:
        if(maior):
            print('Você errou! O seu chute foi maior ')
        elif(menor):
            print('Você errou! O seu chute foi menor ')

    print('Fim do jogo')