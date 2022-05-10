# Para declarar uma função, devemos usar a palavra chave def do mundo Python, seguida pelo nome da função. Lembrando que é consenso usar a nomenclatura snake_case:#
#def nome_da_funcao():
    # todo o código identado faz parte da função print("aprendendo funções")#


import random

def jogar():
    
    imprimir_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letra_acertadas = inicializa_letras_acertadas(palavra_secreta)

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
        print('Você ganhou!! a palavra secreta é {}'.format(palavra_secreta))
    else:
        print('Você perdeu!! a palavra secreta é {}'.format(palavra_secreta))
    print('Fim do jogo')

def imprimir_mensagem_abertura():
        print('_____________________________________________')
        print('________Bem Vindo ao jogo de forca___________')
        print('_____________________________________________') 

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    print('A palavra secreta tem',len (palavra_secreta), 'letras')
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

if(__name__ == "__main__"):
        jogar() 