import random

tentativas = 3 
numero = random.randint(1, 10)

while tentativas > 0:
    palpite = int(input("Digite um numero entre 1 e 10: "))
    if palpite == numero:
        print("Parabens!")
        break
    else:
        tentativas -= 1 
        print(f"vOCE ERROU! TENTATIVAS RESTANTES: {tentativas}")
print(f"O numero era: {numero}")