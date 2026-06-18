print("********************************")
print("bem vindo ao jogo de adivinhação")
print("********************************")

numerosecreto = 40

chute = input("digite seu numero")
print("você digitou: ", chute )

chuteNumerico = int(chute )

acertou = chuteNumerico == numerosecreto
maior = chuteNumerico > numerosecreto
menor = chuteNumerico < numerosecreto

if(numerosecreto == chuteNumerico):
    print("você acertou")
else:
    print("você errou")

print("fim do jogo")