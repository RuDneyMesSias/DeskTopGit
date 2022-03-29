import forca
import adivinhacao

print('_____________________________________________')
print('_________Bem vindo ao jogo de forca__________')
print('_____________________________________________')

print('(1) forca (2) adivinhação')

jogo = int (input('Qual jogo?'))

if(jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando adibinhação")
    adivinhacao.jogar()
