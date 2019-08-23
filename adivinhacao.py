import random

def jogar():
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("Bem vindo no jogo de Adivinhação!")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

    numero_secreto = random.randrange(1, 101)
    # print(numero_secreto)

    total_de_tentativas = 0
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))


    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    print("Tente adivinhar o Número Secreto!")

    pontos = 1000

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite um número de 1 á 100: ")
        print("Você digitou: " + chute)
        chute = int(chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou!, Seu chute é maior que o numero secreto!")
            elif(menor):
                print("Você errou!, Seu chute é menor que o numero secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()