# Para declarar uma função, devemos usar a palavra chave def do mundo Python, seguida pelo nome da função. Lembrando que é consenso usar a nomenclatura snake_case:#
#def nome_da_funcao():
    # todo o código identado faz parte da função print("aprendendo funções")#

def jogar():

    print('_____________________________________________')
    print('________Bem Vindo ao jogo de forca___________')
    print('_____________________________________________')  
    
    palavra_secreta = 'Maça'.upper()
    print('A palavra secreta tem',len (palavra_secreta), 'letras')
    
    letra_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    
    print(letra_acertadas)

    while(not enforcou and not acertou):

        chute = input('Qual letra? ')
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for digito in palavra_secreta:
                if(chute.upper() == digito.upper()):
                    letra_acertadas[index] = digito
                index += 1
        else:
            erros += 1

        enforcou = erros == len(palavra_secreta)
        acertou = '_' not in letra_acertadas
        print(letra_acertadas)

    if(acertou):
        print('Você ganhou!! ')
    else:
        print('Você perdeu!! ')
    print('Fim do jogo')

if(__name__ == "__main__"):
    jogar()
 