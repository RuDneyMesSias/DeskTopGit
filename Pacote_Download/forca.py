# Para declarar uma função, devemos usar a palavra chave def do mundo Python, seguida pelo nome da função. Lembrando que é consenso usar a nomenclatura snake_case:#
#def nome_da_funcao():
    # todo o código identado faz parte da função print("aprendendo funções")#

def jogar():

    print('_____________________________________________')
    print('________Bem vindo ao jogo de forca___________')
    print('_____________________________________________')  
    
    palavra_secreta = 'banana'

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input('Qual letra? ')

        index = 0
        for digito in palavra_secreta:
            if(chute == digito):
                print('Encontrei a letra {} na posição {}'.format(digito, index))
            index = index + 1

        print('jogando ...')

    print('Fim do jogo')

if(__name__ == "__main__"):
    jogar()
 