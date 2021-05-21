import cv2
from os import system, name
from time import sleep

# Limpar a tela do terminal


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

# Desenha o menu de boas vindas


def menu():
    print('')
    print('\033[41m-=-\033[m'*24)
    print(
        '|\033[36m                            Bem Vindo(a)!                            \033[m |')
    print(
        '|\033[36m                     JOGO PEDRA, PAPEL e TESOURA!                    \033[m |')
    print(
        '|\033[36m PEDRA ganha de TESOURA, TESOURA ganha de PAPEL, PAPEL ganha de PEDRA\033[m |')
    print(
        '|\033[1;36m              Digitar "SAIR" para finalizar o jogo\033[m                    |')
    print('\033[41m-=-\033[m'*24)
    print('')


# Apresenta a imagem com a regra do jogo
def image():
    image = cv2.imread('image1.jpg')
    cv2.startWindowThread()
    cv2.imshow('REGRA DO JOGO', image)
    print("Altura (height): %d pixels" % (image.shape[0]))
    print("Altura (width): %d pixels" % (image.shape[1]))
    print("Altura (channels): %d" % (image.shape[2]))

    cv2.waitKey(2500)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
