palavras = input("Digite uma frase: ").lower().split()
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] = contagem[palavra] + 1
    else:
        contagem[palavra] = 1
for palavra, quantidade in contagem.items():
    print(f"{palavra}: {quantidade}")



