import customtkinter
import tkinter as tk
from tkinter import font
from clienteB import cadastrar_cliente
from clienteB import cadastrar_banco
from clienteB import buscar_cpf
from clienteB import sevico_conta
from clienteB import excluir_banco
from clienteB import consulta_extrato
from PIL import Image




from CTkMessagebox import CTkMessagebox
import sqlite3

import sys
import os





class PjPf():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        conn = sqlite3.connect('clientes.db')
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM bancos ")
        except sqlite3.Error as e:
            CTkMessagebox(title="Erro", message=f" Operaçao Cancelada Cadastre uma Agencia antes! {str(e)}",  
                          icon="warning")   
   
        resultadoC = cursor.fetchone()
        nomeC = resultadoC[0]
        
        if nomeC > 0:
            msg = CTkMessagebox(title="Qual tipo de conta ?", message="Pessoa Fisica ou Juridica ?",  
                                    icon="question",option_1="Cancelar", option_3="Fisica", option_2="Juridica")
            response = msg.get()
            
        if response =="Fisica":
        
            self.abrir_cadastro_cliente_PF()
        
        if response == "Juridica":
            self._abrir_cadastro_cliente_Pj()
        



    def abrir_cadastro_cliente_PF(self):
        Cad_pf=customtkinter.CTkToplevel()
        Cad_pf.geometry("500x500")
        Cad_pf.grid_columnconfigure(1, weight=1)
        Cad_pf.grid_rowconfigure(5, weight=0)
        

        f1 = customtkinter.CTkFrame(Cad_pf, width=100, height=50)
        f2 = customtkinter.CTkFrame(Cad_pf, width=100, height=50)
        f3 = customtkinter.CTkFrame(Cad_pf, width=100, height=50)
        f1.grid(row=0, column=0, sticky="nsew")
        f2.grid(row=0, column=1, sticky="nsew")
        f3.grid(row=0, column=2, sticky="nsew")
        
        texto = "Abertura de conta PF"
        label_texto = customtkinter.CTkLabel(f2, text=texto)
        label_texto.pack()

        Cad_pf.title('Cadastro de Cliente')

        label_nome = customtkinter.CTkLabel(Cad_pf, text="Digite seu nome")
        label_nome.grid(row=1,
                        column=0,
                        sticky="nswe", 
                        padx=10, 
                        pady=10)
        self.entry_nome = customtkinter.CTkEntry(Cad_pf, placeholder_text="Digite seu nome completo")
        self.entry_nome.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

        label_cpf = customtkinter.CTkLabel(Cad_pf, text="Digite seu CPF")
        label_cpf.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_cpf = customtkinter.CTkEntry(Cad_pf, placeholder_text="Digite seu CPF")
        self.entry_cpf.grid(row=2, column=1, sticky="nswe", padx=10, pady=10)

        label_endereco = customtkinter.CTkLabel(Cad_pf, text="Digite seu Endereço")
        label_endereco.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_endereco = customtkinter.CTkEntry(Cad_pf, placeholder_text="Digite seu Endereço")
        self.entry_endereco.grid(row=3, column=1, sticky="nswe", padx=10, pady=10)

        label_telefone = customtkinter.CTkLabel(Cad_pf, text="Digite seu telefone")
        label_telefone.grid(row=4, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_telefone = customtkinter.CTkEntry(Cad_pf, placeholder_text="Digite seu telefone")
        self.entry_telefone.grid(row=4, column=1, sticky="nswe", padx=10, pady=10)

        label_email = customtkinter.CTkLabel(Cad_pf, text="Digite seu email")
        label_email.grid(row=5, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_email = customtkinter.CTkEntry(Cad_pf, placeholder_text="Digite seu email")
        self.entry_email.grid(row=5, column=1, sticky="nswe", padx=10, pady=10)

        label_conta = customtkinter.CTkLabel(Cad_pf, text="Digite numero da conta ")
        label_conta.grid(row=8, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_conta = customtkinter.CTkEntry(Cad_pf, placeholder_text="Digite o numero da conta")
        self.entry_conta.grid(row=8, column=1, sticky="nswe", padx=10, pady=10)

        label_ag = customtkinter.CTkLabel(Cad_pf, text="Qual agencia deseja Vincular")
        label_ag.grid(row=6, column=0, sticky="nswe", padx=10, pady=10)

        label_gen = customtkinter.CTkLabel(Cad_pf, text="Qual Gerente vincular")
        label_gen.grid(row=7, column=0, sticky="nswe", padx=10, pady=10)


        self.enviar_dados = customtkinter.CTkButton(Cad_pf, text="Salvar", command=self.cadastrar)
        self.enviar_dados.grid(row=10, column=0, columnspan=2, pady=10)
        
        



        bancos = []
        banco_sel = customtkinter.StringVar(value="Selecione")
        self.entry_bc = customtkinter.CTkOptionMenu(Cad_pf, values=[], variable=banco_sel)
        self.entry_bc.grid(row=6, column=1, sticky="nswe", padx=10, pady=10)
        self.entry_bc.set("")
        self.entry_bc.configure(values=bancos)

        conn = sqlite3.connect('clientes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT banco FROM bancos ")
        
        resultados = cursor.fetchall()
        for resultado in resultados:
            bancos.append(resultado[0])
        self.entry_bc.configure(values=bancos)
        


        gerente= []

        gen_sel = customtkinter.StringVar(value="Selecione")


        self.entry_gen = customtkinter.CTkOptionMenu(Cad_pf, values=[], variable=gen_sel)
        self.entry_gen.grid(row=7, column=1, sticky="nswe", padx=10, pady=10)
        self.entry_gen.set("")
        self.entry_gen.configure(values=gerente)

        conn = sqlite3.connect('clientes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT gerente FROM bancos ")
        resultados_gen = cursor.fetchall()
        for resultado_gen in resultados_gen:
            gerente.append(resultado_gen[0])
        self.entry_gen.configure(values=gerente)

            
            
    def cadastrar(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        endereco = self.entry_endereco.get()
        telefone = self.entry_telefone.get()
        email = self.entry_email.get()
        conta = self.entry_conta.get()
        banco= self.entry_bc.get()
        gerente = self.entry_gen.get()
        saldo="0"
    
        

        
        cadastrar_cliente(self, nome, cpf, endereco, telefone, email, conta,banco,gerente, saldo)

    def _abrir_cadastro_cliente_Pj(self):
        abeturaPJ = customtkinter.CTkToplevel()
        abeturaPJ.geometry("500x500")
        abeturaPJ.grid_columnconfigure(1, weight=1)
        abeturaPJ.grid_rowconfigure(5, weight=0)
        

        f1 = customtkinter.CTkFrame(abeturaPJ, width=100, height=50)
        f2 = customtkinter.CTkFrame(abeturaPJ, width=100, height=50)
        f3 = customtkinter.CTkFrame(abeturaPJ, width=100, height=50)
        f1.grid(row=0, column=0, sticky="nsew")
        f2.grid(row=0, column=1, sticky="nsew")
        f3.grid(row=0, column=2, sticky="nsew")
        texto = "Abertura de conta PJ"
        label_texto = customtkinter.CTkLabel(f2, text=texto)

        texto = font.Font(size=20)
        label_texto.pack()

        abeturaPJ.title('Cadastro de Cliente PJ')

        label_nome = customtkinter.CTkLabel(abeturaPJ, text="Digite seu nome")
        label_nome.grid(row=1,
                        column=0,
                        sticky="nswe", 
                        padx=10, 
                        pady=10)
        self.entry_nome = customtkinter.CTkEntry(abeturaPJ, placeholder_text="Digite a Razão")
        self.entry_nome.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

        label_cpf = customtkinter.CTkLabel(abeturaPJ, text="Digite seu CNPJ")
        label_cpf.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_cpf = customtkinter.CTkEntry(abeturaPJ, placeholder_text="Digite o CPJ")
        self.entry_cpf.grid(row=2, column=1, sticky="nswe", padx=10, pady=10)

        label_endereco = customtkinter.CTkLabel(abeturaPJ, text="Digite o Endereço")
        label_endereco.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_endereco = customtkinter.CTkEntry(abeturaPJ, placeholder_text="Digite o Endereço")
        self.entry_endereco.grid(row=3, column=1, sticky="nswe", padx=10, pady=10)

        label_telefone = customtkinter.CTkLabel(abeturaPJ, text="Digite o telefone")
        label_telefone.grid(row=4, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_telefone = customtkinter.CTkEntry(abeturaPJ, placeholder_text="Digite o telefone")
        self.entry_telefone.grid(row=4, column=1, sticky="nswe", padx=10, pady=10)

        label_email = customtkinter.CTkLabel(abeturaPJ, text="Digite o email")
        label_email.grid(row=5, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_email = customtkinter.CTkEntry(abeturaPJ, placeholder_text="Digite o email")
        self.entry_email.grid(row=5, column=1, sticky="nswe", padx=10, pady=10)

        label_conta = customtkinter.CTkLabel(abeturaPJ, text="Digite numero da conta ")
        label_conta.grid(row=8, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_conta = customtkinter.CTkEntry(abeturaPJ, placeholder_text="Digite o numero da conta")
        self.entry_conta.grid(row=8, column=1, sticky="nswe", padx=10, pady=10)

        label_ag = customtkinter.CTkLabel(abeturaPJ, text="Qual agencia deseja Vincular")
        label_ag.grid(row=6, column=0, sticky="nswe", padx=10, pady=10)

        label_gen = customtkinter.CTkLabel(abeturaPJ, text="Qual Gerente vincular")
        label_gen.grid(row=7, column=0, sticky="nswe", padx=10, pady=10)

        
        bancos = []
        banco_sel = customtkinter.StringVar(value="Selecione")
        self.entry_bc = customtkinter.CTkOptionMenu(abeturaPJ, values=[], variable=banco_sel)
        self.entry_bc.grid(row=6, column=1, sticky="nswe", padx=10, pady=10)
        self.entry_bc.set("")
        self.entry_bc.configure(values=bancos)

        conn = sqlite3.connect('clientes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT banco FROM bancos ")
        
        resultados = cursor.fetchall()
        for resultado in resultados:
            bancos.append(resultado[0])
        self.entry_bc.configure(values=bancos)
        


        gerente= []

        gen_sel = customtkinter.StringVar(value="Selecione")


        self.entry_gen = customtkinter.CTkOptionMenu(abeturaPJ, values=[], variable=gen_sel)
        self.entry_gen.grid(row=7, column=1, sticky="nswe", padx=10, pady=10)
        self.entry_gen.set("")
        self.entry_gen.configure(values=gerente)

        conn = sqlite3.connect('clientes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT gerente FROM bancos ")
        resultados_gen = cursor.fetchall()
        for resultado_gen in resultados_gen:
            gerente.append(resultado_gen[0])
        self.entry_gen.configure(values=gerente)

        
        

        enviar_dados = customtkinter.CTkButton(abeturaPJ, text="Salvar", command=self.cadastrar)
        enviar_dados.grid(row=9, column=0, columnspan=2, pady=10)



class CadastroBanco:
    def __init__(self):
        self.cadastroBanco = customtkinter.CTkToplevel()
        
        self.cadastroBanco.geometry("600x500")
        self.cadastroBanco.grid_columnconfigure(1, weight=1)
        self.cadastroBanco.grid_rowconfigure(5, weight=0)
        

        f1 = customtkinter.CTkFrame(self.cadastroBanco, width=100, height=50)
        f2 = customtkinter.CTkFrame(self.cadastroBanco, width=100, height=50)
        f3 = customtkinter.CTkFrame(self.cadastroBanco, width=100, height=50)
        f1.grid(row=0, column=0, sticky="nsew")
        f2.grid(row=0, column=1, sticky="nsew")
        f3.grid(row=0, column=2, sticky="nsew")
        
        texto = "Cadastro de banco e Agencia e Gerente"
        label_texto = customtkinter.CTkLabel(f2, text=texto)
        label_texto.pack()

        self.cadastroBanco.title('Cadastro de banco e Agencia e Gerente')

        label_nome_banco = customtkinter.CTkLabel(self.cadastroBanco, text="Digite o nome do banco")
        label_nome_banco.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_banco = customtkinter.CTkEntry(self.cadastroBanco, placeholder_text="Nome")
        self.entry_banco.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

        label_ag = customtkinter.CTkLabel(self.cadastroBanco, text="Digite o Numero da agencia")
        label_ag.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_agencia = customtkinter.CTkEntry(self.cadastroBanco, placeholder_text="Numero")
        self.entry_agencia.grid(row=2, column=1, sticky="nswe", padx=10, pady=10)

        label_gerente = customtkinter.CTkLabel(self.cadastroBanco, text="Digite o nome do gerente")
        label_gerente.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_gerente = customtkinter.CTkEntry(self.cadastroBanco, placeholder_text="Nome Completo")
        self.entry_gerente.grid(row=3, column=1, sticky="nswe", padx=10, pady=10)

        salvar_dados = customtkinter.CTkButton(self.cadastroBanco, text="Salvar",command=self.cadastrarBanco)
        salvar_dados.grid(row=9, column=0, columnspan=2, pady=10)
        
        exluir_dados = customtkinter.CTkButton(self.cadastroBanco, text="exluir",command=excluir_banco)
        exluir_dados.grid(row=9, column=1, columnspan=2, pady=10)

    def cadastrarBanco(self):
        banco = self.entry_banco.get()
        agencia = self.entry_agencia.get()
        gerente = self.entry_gerente.get()

    
        cadastrar_banco(self,banco,agencia,gerente)
  


class App(customtkinter.CTk):
    def __init__(self, master=None):
        super().__init__(master)  
        
        self.grid_columnconfigure((0, 1), weight=2)
        self.geometry("600x500")
        customtkinter.set_appearance_mode("dark")
        self.center_window()
        
        button_frame = customtkinter.CTkFrame(self,width=200, height=200)
        button_frame.grid(row=2, column=0, padx=20, pady=20)
        
        abertura_pf = customtkinter.CTkButton(button_frame, text="Abertura de Conta PF/PJ", command=PjPf)
        abertura_pf.grid(row=0, column=0, padx=10, pady=10)
        
        alteracao_conta = customtkinter.CTkButton(button_frame, text="Alteração de conta", command=buscar_cpf)
        alteracao_conta.grid(row=1, column=0, padx=10, pady=10)
        
        cadastro_banco = customtkinter.CTkButton(button_frame, text="Cadastro de Banco", command=CadastroBanco)
        cadastro_banco.grid(row=2, column=0, padx=10, pady=10)
        
        servico_conta = customtkinter.CTkButton(button_frame, text="Serviços de conta", command=sevico_conta)
        servico_conta.grid(row=3, column=0, padx=10, pady=10)
        
        movimentaçao_conta = customtkinter.CTkButton(button_frame, text="Consulta Extrato", command=consulta_extrato)
        movimentaçao_conta.grid(row=4, column=0, padx=10, pady=10)
        
        
        image_frame = customtkinter.CTkFrame(self,width=200, height=200)
        image_frame.grid(row=2, column=1, padx=20, pady=20, sticky="w")
        
        
        my_image = customtkinter.CTkImage(
            dark_image=Image.open('img/dev.png'),
            size=(300, 300)
        )
        
        image_label = customtkinter.CTkLabel(image_frame, image=my_image, text="")
        image_label.pack()
        
        texto_banco = customtkinter.CTkLabel(image_frame, text="Sistema Bancario do Desenvolvedor")
        texto_banco.pack()
        self.iconbitmap("img/icon.ico")
        self.title("Sistema Bancario do Desenvolvedor")
    def center_window(self):
       
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        
        x = int((screen_width - 600) / 2)
        y = int((screen_height - 500) / 2)

       
        self.geometry(f"600x500+{x}+{y}")


app = App()
app.mainloop()
