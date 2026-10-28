primeiro = float(input("Digite o primeiro numero: "))
segundo = float(input("Digite o segundo numero: "))

op = input("Escolha a operação (+, -, *, /): ")

if op == "+":
    print(f"O resultado de {primeiro} + {segundo} é {primeiro + segundo}")
elif op == "-":
    print(f"O resultado de {primeiro} - {segundo} é {primeiro - segundo}")
elif op == "*":
    print(f"O resultado de {primeiro} * {segundo} é {primeiro * segundo}") 
elif op == "/":
    print(f"O resultado de {primeiro} / {segundo} é {primeiro / segundo}")
else:
    print("Operação inválida")

