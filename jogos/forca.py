def jogar():
    print("************************************")
    print("**** Bem vindo no jogo de Forca ****")
    print("************************************")

    palavra_secreta = 'banana'
    acertou = False
    enforcou = False

    # enquanto(True)
    while(not acertou and not enforcou):
        print('jogando...')

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print('Encontrei a letra {} na posição {}'.format(letra,index))
            index +=1




if __name__ == '__main__':
    jogar()