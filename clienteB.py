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
                        gerente TEXT)''')
    
    # cursor.execute("INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?,?,?)", (nome, cpf, endereco, telefone, email ,conta,banco,gerente))
    


    # nome = self.entry_nome.get()
    # cpf = self.entry_cpf.get()
    # endereco = self.entry_endereco.get()
    # telefone = self.entry_telefone.get()
    # email = self.entry_email.get()
    # conta = self.entry_conta.get()
    # banco= self.entry_bc.get()
    # gerente = self.entry_gen.get()

    cursor.execute("SELECT COUNT(*) FROM clientes WHERE cpf = ?", (cpf,))
    
    resultado = cursor.fetchone()
    quantidade_clientes = resultado[0]

    if quantidade_clientes > 0:
        cadstro_invalido = CTkMessagebox(title="Oque deseja fazer ?", message="Cliente ja cadastrado !!",  
                            icon="warning", option_1="Cadastrar Outro Cliente", option_3="sair")
        cadstro_invalido = cadstro_invalido.get()
        
        if response=="sair":
            self.destroy()  

    else:
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
    
    
    
resultado = None    
def buscar_cpf():
    dialog = customtkinter.CTkInputDialog(text="Digite o CPF", title="Buscar CPF")
    cpf = dialog.get_input()
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    AltCliente=customtkinter.CTkToplevel()
    AltCliente.geometry("500x500")
    AltCliente.grid_columnconfigure(1, weight=1)
    AltCliente.grid_rowconfigure(7, weight=0)

    cursor.execute("SELECT * FROM clientes WHERE cpf = ?", (cpf,))
    global resultado

    resultado = cursor.fetchall()

    nome_label = customtkinter.CTkLabel(AltCliente, text="Nome")
    cpf_label = customtkinter.CTkLabel(AltCliente, text="CPF")
    endereco_label = customtkinter.CTkLabel(AltCliente, text="Endereço")
    tel_label = customtkinter.CTkLabel(AltCliente, text="Telefone")
    email_label = customtkinter.CTkLabel(AltCliente, text="Email")
    conta_label = customtkinter.CTkLabel(AltCliente, text="Conta")
    Banco_label = customtkinter.CTkLabel(AltCliente, text="Banco")
    gerente_label = customtkinter.CTkLabel(AltCliente, text="Gerente")

    for i, linha in enumerate(resultado):
        nome_entry = customtkinter.CTkEntry(AltCliente) 
        cpf_entry = customtkinter.CTkEntry(AltCliente)
        endereco_entry = customtkinter.CTkEntry(AltCliente) 
        tel_entry = customtkinter.CTkEntry(AltCliente)        
        email_entry = customtkinter.CTkEntry(AltCliente)         
        conta_entry = customtkinter.CTkEntry(AltCliente)         
        Banco_entry = customtkinter.CTkEntry(AltCliente)         
        gerente_entry = customtkinter.CTkEntry(AltCliente) 


        nome_label.grid(row=0, column=0, padx=10, pady=10)
        nome_entry.grid(row=0, column=1, padx=10, pady=10)
        

        cpf_label.grid(row=1, column=0, padx=10, pady=10)
        cpf_entry.grid(row=1, column=1, padx=10, pady=10)

        endereco_label.grid(row=2, column=0, padx=10, pady=10)
        endereco_entry.grid(row=2, column=1, padx=10, pady=10)

        tel_label.grid(row=3, column=0, padx=10, pady=10)
        tel_entry.grid(row=3, column=1, padx=10, pady=10)

        email_label.grid(row=4, column=0, padx=10, pady=10)
        email_entry.grid(row=4, column=1, padx=10, pady=10)

        conta_label.grid(row=5, column=0, padx=10, pady=10)
        conta_entry.grid(row=5, column=1, padx=10, pady=10)

        Banco_label.grid(row=6, column=0, padx=10, pady=10)
        Banco_entry.grid(row=6, column=1, padx=10, pady=10)
        
        gerente_label.grid(row=7, column=0, padx=10, pady=10)
        gerente_entry.grid(row=7, column=1, padx=10, pady=10)
        
        nome_entry.insert(0, linha[0])
        cpf_entry.insert(0, linha[1])
        endereco_entry.insert(0, linha[2])
        tel_entry.insert(0, linha[3])
        email_entry.insert(0, linha[4])
        conta_entry.insert(0, linha[5])
        Banco_entry.insert(0, linha[6])
        gerente_entry.insert(0, linha[7])

        salvar_button = customtkinter.CTkButton(AltCliente, text="Salvar", command=lambda i=0: salvar_alteracoes(i, cpf_entry.get(),nome_entry.get(),endereco_entry.get(),tel_entry.get(),email_entry.get(),conta_entry.get(),Banco_entry.get(),gerente_entry.get()))
        salvar_button.grid(row=9, column=3, padx=10, pady=10)
        AltCliente.update()
    
    def salvar_alteracoes(i, cpf,novo_nome,novo_endereco,novo_tel,novo_email,novo_conta,novo_banco,novo_gerente):
        cpf = resultado[i][1]
        print(resultado[i])
        novo_nome = nome_entry.get()
        novo_endereco = endereco_entry.get()
        novo_tel = tel_entry.get()
        novo_email = email_entry.get()
        novo_conta = conta_entry.get()
        novo_banco = Banco_entry.get()
        novo_gerente = gerente_entry.get()
        conn = sqlite3.connect('clientes.db')
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE clientes SET nome = ?, endereco = ?, telefone = ?, email = ?, conta = ?, banco = ?, gerente = ? WHERE cpf = ?", (novo_nome, novo_endereco, novo_tel, novo_email, novo_conta, novo_banco, novo_gerente, cpf))
            conn.commit()
            print("Salvo com sucesso no banco de dados")
        except sqlite3.Error as e:
            print("Erro ao salvar os dados no banco de dados:", str(e))
        finally:
            conn.close()
        
        print("salvo com sucesso")

        

        
