import random
from utilidades import clear, menu, image

opcao = ['Tesoura', 'Papel', 'Pedra']
menu()
image()
clear()
menu()

nome = input('Qual seu nome? ').capitalize()

while True:

    robot = random.choice(opcao)
    minhaopcao = input(
        f'{nome}, digite uma das opções (Tesoura/Papel/Pedra): ').strip().capitalize()

    if minhaopcao not in opcao:
        if minhaopcao == 'Sair':
            clear()
            break
        print('Opção inválida!')

    else:
        if robot == minhaopcao:
            print(
                f'\033[32mEMPATOU!!!.\033[m\nO robô escolheu {robot.upper()}.\n{nome} escolheu {minhaopcao.upper()}.')

        elif robot == 'Tesoura' and minhaopcao == 'Papel' or robot == 'Papel' and minhaopcao == 'Pedra' or robot == 'Pedra' and minhaopcao == 'Tesoura':
            print(
                f'\033[31mPERDEU!!!\033[m\nO robô escolheu {robot.upper()}.\n{nome} escolheu {minhaopcao.upper()}.')

        else:
            print(
                f'\033[36mGANHOU, PARABÉNS!!!\033[m\n{nome} escolheu {minhaopcao.upper()}.\nO robô escolheu {robot.upper()}.')
