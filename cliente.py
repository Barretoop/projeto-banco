
clientes = []
contas = []
movimentos = []


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def consultar_saldo(self):
        return self.saldo


class ContaEspecial(Conta):
    def __init__(self, numero, cliente, limite):
        super().__init__(numero, cliente)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")


class Movimento:
    def __init__(self, conta, tipo, valor):
        self.conta = conta
        self.tipo = tipo
        self.valor = valor


def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    cliente = Cliente(nome, cpf)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")


def alterar_cliente():
    cpf = input("Digite o CPF do cliente que deseja alterar: ")
    for cliente in clientes:
        if cliente.cpf == cpf:
            nome = input("Digite o novo nome do cliente: ")
            cliente.nome = nome
            print("Cliente alterado com sucesso!")
            return
    print("Cliente não encontrado.")


def consultar_cliente():
    cpf = input("Digite o CPF do cliente que deseja consultar: ")
    for cliente in clientes:
        if cliente.cpf == cpf:
            print("Nome do cliente:", cliente.nome)
            print("CPF do cliente:", cliente.cpf)
            return
    print("Cliente não encontrado.")


def remover_cliente():
    cpf = input("Digite o CPF do cliente que deseja remover: ")
    for cliente in clientes:
        if cliente.cpf == cpf:
            clientes.remove(cliente)
            print("Cliente removido com sucesso!")
            return
    print("Cliente não encontrado.")


def cadastrar_conta():
    cpf = input("Digite o CPF do cliente para vincular a conta: ")
    for cliente in clientes:
        if cliente.cpf == cpf:
            numero = input("Digite o número da conta: ")
            conta = Conta(numero, cliente)
            contas.append(conta)
            print("Conta cadastrada com sucesso!")
            return
    print("Cliente não encontrado.")
