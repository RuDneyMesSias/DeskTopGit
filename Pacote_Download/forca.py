# Para declarar uma função, devemos usar a palavra chave def do mundo Python, seguida pelo nome da função. Lembrando que é consenso usar a nomenclatura snake_case:#
#def nome_da_funcao():
    # todo o código identado faz parte da função print("aprendendo funções")#


import random



def jogar():
    
    imprimir_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letra_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letra_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto (chute, letra_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == len(palavra_secreta)
        acertou = '_' not in letra_acertadas
        print(letra_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
       imprime_mensagem_perdedor()


       

def imprime_mensagem_vencedor():
    print("Você ganhou")


def imprime_mensagem_perdedor():
    print("Voc~e perdeu")

def marca_chute_correto(chute, letra_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letra_acertadas [index] = letra
        index += 1

def pede_chute():
    chute = input('Qual letra? ')
    chute = chute.strip().upper()
    return chute

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

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

def imprimir_mensagem_abertura():
        print('_____________________________________________')
        print('________Bem Vindo ao jogo de forca___________')
        print('_____________________________________________') 

if(__name__ == "__main__"):
        jogar() 