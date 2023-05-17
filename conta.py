import tkinter as tk
import sqlite3

class Cliente:
    def __init__(self, nome, cpf, endereco, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

class Conta:
    def __init__(self, cliente, numero_conta, saldo):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.saldo = saldo

class ContaCorrente(Conta):
    def __init__(self, cliente, numero_conta, saldo):
        super().__init__(cliente, numero_conta, saldo)

class ContaEspecial(Conta):
    def __init__(self, cliente, numero_conta, saldo, limite):
        super().__init__(cliente, numero_conta, saldo)
        self.limite = limite

def criar_tabela():
    conn = sqlite3.connect('contas.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contas (
                        numero_conta TEXT,
                        tipo TEXT,
                        saldo REAL,
                        cliente TEXT)''')
    conn.commit()
    conn.close()






def cadastrar_conta_corrente():
    numero_conta = entry_numero_conta.get()
    saldo = float(entry_saldo.get())
    cliente = entry_cliente.get()








    conta = ContaCorrente(cliente, numero_conta, saldo)

    conn = sqlite3.connect('contas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contas VALUES (?, ?, ?, ?)", (numero_conta, 'corrente', saldo, cliente))
    conn.commit()
    conn.close()

    print("Conta corrente cadastrada com sucesso!")

def cadastrar_conta_especial():
    numero_conta = entry_numero_conta.get()
    saldo = float(entry_saldo.get())
    limite = float(entry_limite.get())
    cliente = entry_cliente.get()

    conta = ContaEspecial(cliente, numero_conta, saldo, limite)

    conn = sqlite3.connect('contas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contas VALUES (?, ?, ?, ?)", (numero_conta, 'especial', saldo, cliente))
    conn.commit()
    conn.close()

    print("Conta especial cadastrada com sucesso!")

def consultar_saldo():
    numero_conta = entry_consulta_numero_conta.get()

    conn = sqlite3.connect('contas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT saldo, tipo FROM contas WHERE numero_conta=?", (numero_conta,))
    conta = cursor.fetchone()
    conn.close()

    if conta:
        if conta[1] == 'corrente':
            label_consulta_resultado.config(text=f"Conta corrente\nSaldo: R$ {conta[0]}")
        else:
            label_consulta_resultado.config(text=f"Conta especial\nSaldo: R$ {conta[0]}")
    else:
        label_consulta_resultado.config(text="Conta não encontrada")

def consultar_extrato():
    numero_conta = entry_consulta_numero_conta.get()

    conn = sqlite3.connect('contas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT tipo, saldo, cliente FROM contas WHERE numero_conta=?", (numero_conta,))
    conta = cursor.fetchone()
    conn.close()

    if conta:
        if conta[0] == 'corrente':
            tipo_conta = "Conta corrente"
        else:
            tipo_conta = "Conta especial"
        
        extrato = f"{tipo_conta}\nSaldo: R$ {conta[1]}\nCliente: {conta[2]}\n\nMovimentações:\n"
        # Aqui você pode adicionar as movimentações da conta corrente ou especial
        
        label_consulta_resultado.config(text=extrato)
    else:
        label_consulta_resultado.config(text="Conta não encontrada")

# Criar a janela do Tkinter
janela = tk.Tk()

# Criar os widgets (campos de entrada, botões, rótulos)
label_numero_conta = tk.Label(janela, text="Número da conta:")
label_numero_conta.pack()
entry_numero_conta = tk.Entry(janela)
entry_numero_conta.pack()

label_saldo = tk.Label(janela, text="Saldo:")
label_saldo.pack()
entry_saldo = tk.Entry(janela)
entry_saldo.pack()

label_limite = tk.Label(janela, text="Limite (somente para conta especial):")
label_limite.pack()
entry_limite = tk.Entry(janela)
entry_limite.pack()

label_cliente = tk.Label(janela, text="Cliente:")
label_cliente.pack()
entry_cliente = tk.Entry(janela)
entry_cliente.pack()

botao_cadastrar_corrente = tk.Button(janela, text="Cadastrar Conta Corrente", command=cadastrar_conta_corrente)
botao_cadastrar_corrente.pack()

botao_cadastrar_especial = tk.Button(janela, text="Cadastrar Conta Especial", command=cadastrar_conta_especial)
botao_cadastrar_especial.pack()

label_consulta_numero_conta = tk.Label(janela, text="Número da conta:")
label_consulta_numero_conta.pack()
entry_consulta_numero_conta = tk.Entry(janela)
entry_consulta_numero_conta.pack()

botao_consultar_saldo = tk.Button(janela, text="Consultar Saldo", command=consultar_saldo)
botao_consultar_saldo.pack()

botao_consultar_extrato = tk.Button(janela, text="Consultar Extrato", command=consultar_extrato)
botao_consultar_extrato.pack()

label_consulta_resultado = tk.Label(janela)
label_consulta_resultado.pack()

# Iniciar o loop principal do Tkinter
janela.mainloop()