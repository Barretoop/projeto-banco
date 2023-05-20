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

def cadastrar_cliente(self, nome, cpf, endereco, telefone, email, conta, banco, gerente):
    
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
                        conta TEXT,
                        banco TEXT,
                        gerente)''')
    
    cursor.execute("INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?,?,?)", (nome, cpf, endereco, telefone, email ,conta,banco,gerente))
    
    nome = self.entry_nome.get()
    cpf = self.entry_cpf.get()
    endereco = self.entry_endereco.get()
    telefone = self.entry_telefone.get()
    email = self.entry_email.get()
    conta = self.entry_conta.get()
    banco= self.entry_bc.get()
    gerente = self.entry_gen.get()

            
    
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
    
    
    
            
def buscar_cpf(self,cpf):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    AltCliente=customtkinter.CTkToplevel()
    cursor.execute("SELECT * FROM clientes WHERE cpf = ?", (cpf,))
    resultado = cursor.fetchall()
    cpf = self.entry_cpf.get()
    for i, linha in enumerate(resultado):
            
            entry = customtkinter.CTkLabel(AltCliente,text=linha[0]) 
            entry.grid(row=i, column=0)
            
    # for i, linha in enumerate(resultado):
    #         for j, valor in enumerate(linha):
    #             entry = customtkinter.CTkEntry(AltCliente)
    #             entry.insert(valor)
    #             entry.grid(row=i+1, column=j)
    print(resultado)
    conn.close()