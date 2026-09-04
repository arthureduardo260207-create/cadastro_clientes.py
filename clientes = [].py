import json

clientes = []


# CADASTRAR CLIENTES (1)
def cadastrar_cliente():
    print("Voce escolheu cadastrar um cliente")

    while True:
        nome = input("Digite o nome do cliente: ")

        if nome:
            break
        else:
            print("Digite um nome válido.")

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

    salvar_clientes()

    print("Cliente cadastrado com sucesso!")


# LISTAR CLIENTES (2)
def listar_clientes():
    print("Voce escolheu listar clientes")

    if clientes:
        for numero, cliente in enumerate(clientes, start=1):
            print("Cliente", numero)
            print("Nome:", cliente["nome"])
            print("Idade:", cliente["idade"])
            print("Telefone:", cliente["telefone"])
            print("--------------------")
    else:
        print("Não existem clientes cadastrados.")


# EXCLUIR CLIENTES (3)
def excluir_clientes():
    print("Voce escolheu excluir clientes")

    if clientes:

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


# EDITAR CLIENTES (4)
def editar_cliente():
    print("Voce escolheu editar clientes")

    if clientes:
        while True:
            try:
                numero = int(input("Digite o número do cliente que deseja editar: "))
                break
            except ValueError:
                print("Digite um número válido.")

        if numero >= 1 and numero <= len(clientes):

            cliente = clientes[numero - 1]

            print("Cliente encontrado:", cliente["nome"])

            # EDITAR NOME
            while True:
                novo_nome = input("Digite o novo nome: ")

                if novo_nome:
                    cliente["nome"] = novo_nome
                    break
                else:
                    print("Digite um nome válido.")

            # EDITAR IDADE
            while True:
                try:
                    nova_idade = int(input("Digite a nova idade: "))

                    if nova_idade > 0:
                        cliente["idade"] = nova_idade
                        break
                    else:
                        print("A idade deve ser maior que 0.")

                except ValueError:
                    print("Digite uma idade válida.")

            # EDITAR TELEFONE
            while True:
                novo_telefone = input("Digite o novo telefone: ")

                if novo_telefone.isdigit() and (
                    len(novo_telefone) == 10 or len(novo_telefone) == 11
                ):
                    cliente["telefone"] = novo_telefone
                    break
                else:
                    print("Digite um telefone válido.")

            print("Cliente editado com sucesso!")

        else:
            print("Número de cliente inválido.")

    else:
        print("Não existem clientes cadastrados.")


# ==== MENU ====
executando = True

while executando:
    print("== SISTEMA DE CADASTRO DE CLIENTES ===")
    print("1 - Cadastrar clientes")
    print("2 - Listar clientes")
    print("3 - Excluir cliente")
    print("4 - Editar cliente")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        listar_clientes()

    elif opcao == "3":
        excluir_clientes()

    elif opcao == "4":
        editar_cliente()

    elif opcao == "5":
        print("Programa encerrado")
        executando = False

    else:
        print("Opção inválida")
