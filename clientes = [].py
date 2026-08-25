clientes = []

executando = True

while executando:
    print("== SISTEMA DE CADASTRO DE CLIENTES ===")
    print("1 - Cadastrar clientes")
    print("2 - Listar clientes")
    print("3 - Excluir cliente")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Você escolheu cadastrar um cliente")

        while True:
            nome = input("Digite o nome do cliente: ")

            if nome:
                break

        while True:
            try:
                idade = int(input("Digite a idade do cliente: "))

                if idade > 0:
                    break
                else:
                    print("A idade deve ser maior que 0.")

            except ValueError:
                print("Digite uma idade válida.")

        while True:
            telefone = input("Digite o telefone do cliente: ")

            if telefone.isdigit() and (len(telefone) == 10 or len(telefone) == 11):
                break
            else:
                print("Digite um telefone válido.")

        cliente = {
            "nome": nome,
            "idade": idade,
            "telefone": telefone
        }

        clientes.append(cliente)

    elif opcao == "2":
        print("Você escolheu listar clientes")

        if clientes:
            for numero, cliente in enumerate(clientes, start=1):
                print("Cliente", numero)
                print("Nome:", cliente["nome"])
                print("Idade:", cliente["idade"])
                print("Telefone:", cliente["telefone"])
        else:
            print("Não existem clientes cadastrados.")

    elif opcao == "3":

        if clientes:
            print("Você escolheu excluir clientes")

            while True:
                try:
                    numero = int(input("Digite o número do cliente que deseja excluir: "))
                    break
                except ValueError:
                    print("Digite um número válido.")

            if numero >= 1 and numero <= len(clientes):
                cliente_excluido = clientes.pop(numero - 1)

                print("Cliente", cliente_excluido["nome"], "excluído com sucesso!")
            else:
                print("Número de cliente inválido.")

        else:
            print("Não existem clientes cadastrados.")

    elif opcao == "4":
        print("Programa encerrado")
        executando = False

    else:
        print("Opção inválida")