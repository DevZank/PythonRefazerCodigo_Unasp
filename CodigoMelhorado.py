from random import randint

print (" ======= Bem vindo ao Jogo de Adivinhação ======= \n")

random = randint(0, 100)
chute = 0

for chances in range(9, 0, -1):
    chute = int(input("Digite um número entre 0 a 100: "))
    
    if chute > 100 or chute < 0:
        while (chute > 100 or chute < 0):
            print("Você digitou um número diferente do informado!")
            chute = int(input("Digite novamente um número entre 0 a 100: "))
        if chute == random:
            print("\nParabéns, você venceu! O número era {} e você ainda tinha {} chances.\n".format(random, chances))
            break
        else:
            if chute > random:
                print('\nVocê errou!!! Dica: É um número menor.')
            else:
                print('Você errou!!! Dica: É um número maior.')
            print('Você ainda possui {} chances.\n'.format(chances))
        if chances == 0:
            print('\nSuas chances acabaram, você perdeu!\n')
            break;

print ("\n ======= Fim de Jogo ======= ")