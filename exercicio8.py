tarefas = []

while True:
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nova = input("Digite a tarefa: ")
        tarefas.append(nova)
    elif escolha == "2":
        if tarefas:
            for numero, item in enumerate(tarefas, 1):
                print(f"{numero}. {item}")
        else:
            print("Nenhuma tarefa ainda")
    elif escolha == "3":
        print("Até logo!")
        break
    else:
        print("Opção inválida")
