from asyncore import ExitNow
import forca
import adivinhacao

print('_____________________________________________')
print('_________Bem vindo ao jogo de forca__________')
print('_____________________________________________')

print('(1) Forca (2) Adivinhação')

jogo = int (input('Qual jogo?'))
ExitNow

if(jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando adivinhação")
    adivinhacao.jogar()
