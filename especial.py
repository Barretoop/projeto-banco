import cliente


def cadastrar_conta_especial():
    cpf = input("Digite o CPF do cliente para vincular a conta especial: ")
    for cliente in cliente.clientes:
        if cliente.cpf == cpf:
            numero = input("Digite o número da conta especial: ")
            limite = float(input("Digite o limite da conta especial: "))
            conta_especial = cliente.ContaEspecial(numero, cliente, limite)
            cliente.contas.append(conta_especial)
            print("Conta especial cadastrada com sucesso!")
            return
