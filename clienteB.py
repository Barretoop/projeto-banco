import tkinter as tk
import sqlite3
import customtkinter
from CTkMessagebox import CTkMessagebox



class Cliente:
    def __init__(self, nome, cpf, endereco, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

def cadastrar_cliente(self, nome, cpf, endereco, telefone, email, conta):
    
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT count(*) FROM sqlite_master WHERE type='table' AND name='clientes'
    """)
    tabela_existe = cursor.fetchone()[0]

    if not tabela_existe:
            cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        nome TEXT,
                        cpf TEXT,
                        endereco TEXT,
                        telefone TEXT,
                        email TEXT,
                        conta TEXT)''')
    
    cursor.execute("INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?)", (nome, cpf, endereco, telefone, email ,conta))
    
    nome = self.entry_nome.get()
    cpf = self.entry_cpf.get()
    endereco = self.entry_endereco.get()
    telefone = self.entry_telefone.get()
    email = self.entry_email.get()
    conta = self.entry_conta.get()

            
    
    conn.commit()
    conn.close()

    msg = CTkMessagebox(title="Oque deseja fazer ?", message="Cliente cadastrado com Sucesso 1",  
                        icon="check", option_1="Cadastrar Outro Cliente", option_3="sair")
    response = msg.get()
    
    if response=="sair":
        self.destroy()       



class Banco:
      def __init__(self, banco, agencia, gerente):
        self.banco = banco
        self.agencia = agencia
        self.gerente = gerente
        
def cadastrar_banco(self, banco,agencia,gerente ) :
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT count(*) FROM sqlite_master WHERE type='table' AND name='bancos'
    """)
    tabela_existe = cursor.fetchone()[0]

    if not tabela_existe:
            cursor.execute('''CREATE TABLE IF NOT EXISTS bancos (
                        banco TEXT,
                        agencia TEXT,
                        gerente TEXT)''')
            

    cursor.execute("INSERT INTO bancos VALUES (?, ?, ?)", (banco,agencia,gerente))

    banco = self.entry_banco.get()
    agencia = self.entry_agencia.get()
    gerente = self.entry_gerente.get()
    conn.commit()
    conn.close()
    
    
    msg = CTkMessagebox(title="Oque deseja fazer ?", message="Banco cadastrado com Sucesso !",  
                        icon="check", option_1="Cadastrar Outro Cliente", option_3="sair")
    response = msg.get()
    
    if response=="sair":
        self.destroy()  
    
    
    
            

# def consultar_cliente():
#     cpf = entry_consulta_cpf.get()

#     conn = sqlite3.connect('clientes.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM clientes WHERE cpf=?", (cpf,))
#     cliente = cursor.fetchone()
#     conn.close()

#     if cliente:
#         label_consulta_resultado.config(text=f"Nome: {cliente[0]}\nCPF: {cliente[1]}\nEndereço: {cliente[2]}\nTelefone: {cliente[3]}\nEmail: {cliente[4]}")
#     else:
#         label_consulta_resultado.config(text="Cliente não encontrado")

# def remover_cliente():
#     cpf = entry_remocao_cpf.get()

#     conn = sqlite3.connect('clientes.db')
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM clientes WHERE cpf=?", (cpf,))
#     conn.commit()
#     conn.close()

#     print("Cliente removido com sucesso!")