# Para declarar uma função, devemos usar a palavra chave def do mundo Python, seguida pelo nome da função. Lembrando que é consenso usar a nomenclatura snake_case:#
#def nome_da_funcao():
    # todo o código identado faz parte da função print("aprendendo funções")#

def jogar():

    print('_____________________________________________')
    print('________Bem vindo ao jogo de forca___________')
    print('_____________________________________________')  
    
    palavra_secreta = 'mel'
    print('A palavra secreta tem',len (palavra_secreta), 'letras')
    letra_acertadas = ['_', '_', '_', '_', '_', '_']

    enforcou = False
    acertou = False
    erros = 0
    
    print(letra_acertadas)

    while(not enforcou and not acertou):

        chute = input('Qual letra? ')
        chute = chute.strip()

        if(chute in palavra_secreta):
            index = 0
            for digito in palavra_secreta:
                if(chute.upper() == digito.upper()):
                    letra_acertadas[index] = digito
                index = index + 1
        else:
            erros = erros + 1

        enforcou = erros == len(palavra_secreta)
        print(letra_acertadas)

    print('Fim do jogo')

if(__name__ == "__main__"):
    jogar()
 