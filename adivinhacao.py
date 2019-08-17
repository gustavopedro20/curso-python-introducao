print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Bem vindo no jogo de Adivinhação!")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

print("Tente adivinhar o Número Secreto!")


while(rodada <= total_de_tentativas > 0):
    print("Tentativa", rodada, "de", total_de_tentativas)
    chute = input("Digite seu numero: ")
    print("Você digitou: " + chute)
    chute = int(chute)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou!, Seu chute é maior que o numero secreto!")
        elif(menor):
            print("Você errou!, Seu chute é menor que o numero secreto!")
    rodada = rodada + 1


print("Fim do jogo!")