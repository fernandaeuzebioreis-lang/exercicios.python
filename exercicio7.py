import random

secreto = random.randint(1, 20)
tentativas = 0
palpite = 0

while palpite != secreto:
    palpite = int(input("Escolha um número: "))
    tentativas = tentativas + 1
    if palpite > secreto:
        print("Seu palpite é maior")
    elif palpite < secreto:
        print("Seu palpite é menor")

print(f"Acertou em {tentativas} tentativas!")