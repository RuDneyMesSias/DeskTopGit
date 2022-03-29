import random

print('_____________________________________________')
print('Bem vindo ao jogo de advinhação ')
print('_____________________________________________')

numero_secreto = random.randrange(1,101)
totativa = 0
pontua = 1000

print('Qual nível de dificuldade?')
print('(1) Fácil (2) Médio (3) Difícil')

nivel = int(input('Define o nível: '))

if(nivel == 1):
    totativa = 20
elif(nivel == 2):
    totativa = 10
else:
    totativa = 5

for rodada in range(1, totativa + 1):
    print('Tentativa {} de {}'.format(rodada, totativa))

    chute_str = input('Digite seu número ')
    print('Você digitou', chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print('Você deve digitar um número entre 1 e 100!')
        continue

    acertou = chute == numero_secreto
    maior   = chute  > numero_secreto   
    menor   = chute  < numero_secreto

    if(acertou):
        print('Você acertou {} pontos!'. format(pontos))
        break
    else:
        if(maior):
            print('Você errou! O seu chute foi maior ')
        elif(menor):
            print('Você errou! O seu chute foi menor ')
        
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontua - pontos_perdidos

    print('Fim do jogo')
