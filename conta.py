import cliente


def consultar_saldo():
    numero_conta = input("Digite o número da conta: ")
    for conta in cliente.contas:
        if conta.numero == numero_conta:
            saldo = conta.consultar_saldo()
            print("Saldo da conta:", saldo)
            return
    print("Conta não encontrada.")


def realizar_deposito():
    numero_conta = input("Digite o número da conta: ")
    for conta in cliente.contas:
        if conta.numero == numero_conta:
            valor = float(input("Digite o valor do depósito: "))
            conta.depositar(valor)
            movimento = cliente.Movimento(conta, "Depósito", valor)
            cliente.movimentos.append(movimento)
            print("Depósito realizado com sucesso!")
            return
    print("Conta não encontrada.")


def realizar_saque():
    numero_conta = input("Digite o número da conta: ")
    for conta in cliente.contas:
        if conta.numero == numero_conta:
            valor = float(input("Digite o valor do saque: "))
            conta.sacar(valor)
            movimento = cliente.Movimento(conta, "Saque", valor)
            cliente.movimentos.append(movimento)
            print("Saque realizado com sucesso!")
            return
    print("Conta não encontrada.")


def consultar_extrato():
    numero_conta = input("Digite o número da conta: ")
    for conta in cliente.contas:
        if conta.numero == numero_conta:
            print("Extrato da conta:")
            for movimento in cliente.movimentos:
                if movimento.conta == conta:
                    print("Tipo:", movimento.tipo)
                    print("Valor:", movimento.valor)
            return
    print("Conta não encontrada.")
