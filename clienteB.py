import tkinter as tk
import sqlite3
import customtkinter
from datetime import datetime
from PIL import Image

from CTkMessagebox import CTkMessagebox


class Cliente:
    def __init__(self, nome, cpf, endereco, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

def cadastrar_cliente(self, nome, cpf, endereco, telefone, email, conta, banco, gerente, saldo):
    
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
                        gerente TEXT,
                        saldo TEXT)''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS movimentacao (
                        nome TEXT,
                        cpf TEXT,
                        tipo_movimentacao TEXT,
                        data TEXT,
                        saldo TEXT)''')
    

    cursor.execute("SELECT COUNT(*) FROM clientes WHERE cpf = ?", (cpf,))
    
    resultado = cursor.fetchone()
    quantidade_clientes = resultado[0]

    if quantidade_clientes > 0:
        cadastro_invalido = CTkMessagebox(title="Oque deseja fazer ?", message="Cliente ja cadastrado !!",  
                            icon="warning", option_1="Cadastrar outro Cliente", option_3="sair")
        cadastro_invalido = cadastro_invalido.get()
        
        if response=="sair":
            cadastro_invalido.destroy()  

    else:
        cursor.execute("INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (nome, cpf, endereco, telefone, email ,conta,banco,gerente,saldo))
    


        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        endereco = self.entry_endereco.get()
        telefone = self.entry_telefone.get()
        email = self.entry_email.get()
        conta = self.entry_conta.get()
        banco= self.entry_bc.get()
        gerente = self.entry_gen.get()
        saldo = "0"          
        
        conn.commit()
        conn.close()

        msg = CTkMessagebox(title="Oque deseja fazer ?", message="Cliente cadastrado com Sucesso 1",  
                            icon="check", option_1="Cadastrar Outro Cliente", option_3="sair")
        response = msg.get()
        
        if response=="sair":
            self.destroy()       


resultado = None    

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
                        icon="check", option_1="Cadastrar Outro Banco ?", option_3="sair")
    response = msg.get()
    
    if response=="sair":
        msg.destroy()  


def excluir_banco():
    dialog = customtkinter.CTkInputDialog(text="Confirme o Agencia", title="Buscar Banco")
    banco = dialog.get_input()
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM bancos WHERE agencia = ?", (banco,))
    resultadoC = cursor.fetchone()
    nomeC = resultadoC[0]
    if nomeC > 0:
        cursor.execute("SELECT * FROM bancos WHERE agencia = ?", (banco,))
        
        resultado = cursor.fetchone()
        nome = resultado[0]
        msg = CTkMessagebox(title="Tem Certeza que deseja excluir Ag ?", message=f"Nome do Banco  : {nome} ",
                        icon="warning",option_1="Sim",option_2="Cancelar Operação")
        response = msg.get()
              
        if response == "Sim":
            try:
                cursor.execute("DELETE FROM bancos WHERE agencia = ?", (banco,))
                conn.commit()
                CTkMessagebox(title="check", message="Agencia Excluida")
            except sqlite3.Error as e:
                CTkMessagebox(title="Info", message=f" Erro : {str(e)}")
            finally:
                conn.close()    
        elif response == "Cancelar Operação":
            CTkMessagebox(title="warning", message="Operaçao Cancelada !")
    else:
        CTkMessagebox(title="warning", message="Agencia Não encontrada !")

def excluir_cliente():
    dialog = customtkinter.CTkInputDialog(text="Confirme o CPF/CNPJ ", title="Buscar CPF/CNPJ")
    cpf = dialog.get_input()
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE cpf = ?", (cpf,))
    resultado = cursor.fetchone()
    nome = resultado[0]
    msg = CTkMessagebox(title="Tem Certeza que deseja Excluir o cliente ? !", message=f"Nome do Cliente  : {nome} ",
                    icon="warning",option_1="Sim",option_2="Cancelar Operação")
    response = msg.get()
    
    if response == "Sim":
        try:
            cursor.execute("DELETE FROM clientes WHERE cpf = ?", (cpf,))
            conn.commit()
            CTkMessagebox(title="check", message="Cliente Excluido")
        except sqlite3.Error as e:
                    CTkMessagebox(title="Info", message=f" Erro : {str(e)}")
        finally:
            conn.close()    
    elif response == "Cancelar Operação":
        CTkMessagebox(title="warning", message="Operaçao Cancelada !")

def buscar_cpf():
    dialog = customtkinter.CTkInputDialog(text="Digite o CPF ", title="Buscar CPF")
    cpf = dialog.get_input()
    
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    AltCliente=customtkinter.CTkToplevel()
    AltCliente.geometry("500x500")
    AltCliente.grid_columnconfigure(1, weight=1)
    AltCliente.grid_rowconfigure(7, weight=0)
    AltCliente.title('Cadastro de Cliente')
    
    
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
    saldo_label = customtkinter.CTkLabel(AltCliente, text="Gerente")
    

    for i, linha in enumerate(resultado):
        nome_entry = customtkinter.CTkEntry(AltCliente) 
        cpf_entry = customtkinter.CTkEntry(AltCliente)
        endereco_entry = customtkinter.CTkEntry(AltCliente) 
        tel_entry = customtkinter.CTkEntry(AltCliente)        
        email_entry = customtkinter.CTkEntry(AltCliente)         
        conta_entry = customtkinter.CTkEntry(AltCliente)         
        Banco_entry = customtkinter.CTkEntry(AltCliente)         
        gerente_entry = customtkinter.CTkEntry(AltCliente) 
        saldo_entry = customtkinter.CTkEntry(AltCliente) 
        


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
        
        saldo_label.grid(row=8, column=0, padx=10, pady=10)
        saldo_entry.grid(row=8, column=1, padx=10, pady=10)
        
        nome_entry.insert(0, linha[0])
        cpf_entry.insert(0, linha[1])
        endereco_entry.insert(0, linha[2])
        tel_entry.insert(0, linha[3])
        email_entry.insert(0, linha[4])
        conta_entry.insert(0, linha[5])
        Banco_entry.insert(0, linha[6])
        gerente_entry.insert(0, linha[7])
        saldo_entry.insert(0, linha[8])
        
        saldo_entry.configure(state="disable") 

        excluir_button = customtkinter.CTkButton(AltCliente, text="Excluir", command=excluir_cliente)
        excluir_button.grid(row=9, column=3, padx=10, pady=10)    
            
        salvar_button = customtkinter.CTkButton(AltCliente, text="Salvar", command=lambda i=0: salvar_alteracoes(i, cpf_entry.get(),nome_entry.get(),endereco_entry.get(),tel_entry.get(),email_entry.get(),conta_entry.get(),Banco_entry.get(),gerente_entry.get()))
        salvar_button.grid(row=8, column=3, padx=10, pady=10)
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
            CTkMessagebox(title="check", message="Salvo com Sucesso")
        except sqlite3.Error as e:
            CTkMessagebox(title="Info", message=f" Erro : {str(e)}")
        finally:
            conn.close()
        
        

        
def sevico_conta():
    dialog = customtkinter.CTkInputDialog(text="Digite o CPF/CNPJ", title="Buscar CPF/CNPJ")
    cpf = dialog.get_input()
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE cpf = ?", (cpf,))
    global resultado
    resultado = cursor.fetchone()
    nome = resultado[0]
    msg = CTkMessagebox(title="Verifique se e o cliente/Razão correto ?", message=f"Nome do Cliente/Razão  : {nome} ",
                    icon="question", option_1="Esta correto", option_2="Não esta Correto")
    response = msg.get()
    
    if response == "Esta correto":
        msg = CTkMessagebox(title="Oque Deseja fazer ?", message="Escolha o Seviço desejado ! ?",  
                                icon="question",option_1="Deposito", option_3="Saque", option_2="Saldo Atual")
        response = msg.get()
    
        
        if response == "Deposito":
            saldoV = resultado[8]
            msg = CTkMessagebox(title="Saldo Bancario !", message=f"Saldo do Cliente/Razão  : {saldoV}.00 R$ ",
                    icon="info")
            response = msg.get()
            deposito = customtkinter.CTkInputDialog(text="O valor que deseja depositar", title="Deposito")
            deposito = deposito.get_input() 
            conn = sqlite3.connect('clientes.db')
            cursor = conn.cursor()
            try:
                cursor.execute("UPDATE clientes SET saldo = saldo + ? WHERE cpf = ?", (deposito, cpf))
                conn.commit()
                data_atual = datetime.now().strftime('%d-%m-%Y')
                nome_cliente = resultado[0]
                cursor.execute("INSERT INTO movimentacao (nome, cpf, tipo_movimentacao, saldo, data) VALUES (?, ?, ?, ?, ?)", (nome_cliente, cpf,  'Depósito', deposito, data_atual))
                conn.commit()
                CTkMessagebox(title="check", message="Deposito Efetuado !")
            except sqlite3.Error as e:
                CTkMessagebox(title="Info", message=f" Erro : {str(e)}")
            finally:
                conn.close()
            
           
        
        if response == "Saque":                  
            saldoV = resultado[8]
            msg = CTkMessagebox(title="Saldo Bancario !", message=f"Saldo do Cliente/Razão  : {saldoV}.00 R$ ",
                    icon="info")
            response = msg.get()
            sacar = customtkinter.CTkInputDialog(text="O valor que deseja Sacar", title="sacar")
            sacar = sacar.get_input() 
            conn = sqlite3.connect('clientes.db')
            cursor = conn.cursor()
            try:
                cursor.execute("UPDATE clientes SET saldo = saldo - ? WHERE cpf = ?", (sacar, cpf))
                conn.commit()
                data_atual = datetime.now().strftime('%d-%m-%Y')
                nome_cliente = resultado[0]
                cursor.execute("INSERT INTO movimentacao (nome, cpf, tipo_movimentacao, saldo, data) VALUES (?, ?, ?, ?, ?)", (nome_cliente, cpf,  'Saque', sacar, data_atual))
                conn.commit()
                cursor.execute("SELECT saldo FROM clientes WHERE cpf = ?", (cpf,))
                Nsaldo = cursor.fetchone()
                saldoN = Nsaldo[0]
                print("Salvo com sucesso no banco de dados")
                msg = CTkMessagebox(title="Novo Saldo Bancario !", message=f"Saldo do Cliente/Razão  : {saldoN}.00 R$ ",
                    icon="check")
            except sqlite3.Error as e:
                CTkMessagebox(title="Info", message=f" Erro : {str(e)}")
            finally:
                conn.close()
            
            
        
        if response == "Saldo Atual":
                cursor.execute("SELECT saldo FROM clientes WHERE cpf = ?", (cpf,))
                Nsaldo = cursor.fetchone()
                saldoN = Nsaldo[0]
                msg = CTkMessagebox(title="Saldo Bancario !", message=f"Saldo do Cliente/Razão  : {saldoN}.00 R$ ",
                    icon="info")
            
def consulta_extrato():
    dialog = customtkinter.CTkInputDialog(text="Digite o CPF/CNPJ", title="Buscar CPF/CNPJ")
    cpf = dialog.get_input()
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE cpf = ?", (cpf,))
    global resultado
    resultado = cursor.fetchone()
    nome = resultado[0]
    msg = CTkMessagebox(title="Verifique se e o cliente/Razão correto ?", message=f"Nome do Cliente/Razão  : {nome} ",
                    icon="question", option_1="Esta correto", option_2="Não esta Correto")
    response = msg.get()
    if response == "Esta correto":
            try:
                cursor.execute("SELECT * FROM movimentacao WHERE cpf = ?", (cpf,))
                movimentacoes = cursor.fetchall()
                MovCliente=customtkinter.CTkToplevel()
                MovCliente.geometry("800x500")
                MovCliente.grid_columnconfigure(1, weight=1)
                MovCliente.grid_rowconfigure(7, weight=0)
                MovCliente.iconbitmap("img\icon.ico")
                
                scrollable_frame = customtkinter.CTkScrollableFrame(MovCliente,
                                                                    width=700, 
                                                                    height=400)
                scrollable_frame.grid(row=0, column=0, padx=20, pady=20)  
                
                top_bar = customtkinter.CTkFrame(scrollable_frame)
                top_bar.grid(row=0, column=0, sticky="ew")
                
                column_labels = ["Nome","CPF","Tipo de Movimentação", "Data", "Valor"]
                for i, column_name in enumerate(column_labels):
                    label = customtkinter.CTkLabel(top_bar, text=column_name)
                    label.grid(row=0, column=i, padx=10, pady=5, sticky="w")
                    
                mov_frame = customtkinter.CTkFrame(scrollable_frame)
                mov_frame.grid(row=1, column=0, sticky="nsew")
                
                for i, movimentacao in enumerate(movimentacoes):
                    nomeC = movimentacao[0]
                    Cpf = movimentacao[1]
                    tipo_movimentacao = movimentacao[2]
                    valor = movimentacao[3]
                    data = movimentacao[4]
                    
                    label_nome = customtkinter.CTkLabel(mov_frame, text=f" {nomeC} ")
                    label_nome.configure(anchor="center", justify="center")
                    label_nome.grid(row=i, column=0, padx=10, pady=5, sticky="ew")
                    
                    label_cpf = customtkinter.CTkLabel(mov_frame, text=f" {Cpf} ")
                    label_cpf.configure(anchor="center", justify="center")
                    label_cpf.grid(row=i, column=1, padx=10, pady=5,sticky="ew")
                    
                    label_tipo = customtkinter.CTkLabel(mov_frame, text=f" {tipo_movimentacao} ")
                    label_tipo.configure(anchor="center", justify="center")
                    label_tipo.grid(row=i, column=2, padx=10, pady=5, sticky="ew")

                    label_valor = customtkinter.CTkLabel(mov_frame, text=f" {valor} ")
                    label_valor.configure(anchor="center", justify="center")
                    label_valor.grid(row=i, column=3, padx=10, pady=5, sticky="ew")

                    label_data = customtkinter.CTkLabel(mov_frame, text=f" {data}.00R$ ")
                    label_data.configure(anchor="center", justify="center")
                    label_data.grid(row=i, column=4, padx=10, pady=5, sticky="ew")

            except sqlite3.Error as e:
                CTkMessagebox(title="Info", message=f"Erro: {str(e)}")
            finally:
                conn.close()

    
    
    
    
    
    
        
        
    