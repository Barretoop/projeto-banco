import customtkinter
from tkinter import * 
import tkinter as tk
from tkinter import font
from clienteB import cadastrar_cliente


customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  
# app=tk.Tk()




class CadastroCliente():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.abertura=customtkinter.CTkToplevel()
        self.abertura.geometry("600x500")
        self.abertura.grid_columnconfigure(1, weight=1)
        self.abertura.grid_rowconfigure(5, weight=0)

        f1 = customtkinter.CTkFrame(self.abertura, width=100, height=50)
        f2 = customtkinter.CTkFrame(self.abertura, width=100, height=50)
        f3 = customtkinter.CTkFrame(self.abertura, width=100, height=50)
        f1.grid(row=0, column=0, sticky="nsew")
        f2.grid(row=0, column=1, sticky="nsew")
        f3.grid(row=0, column=2, sticky="nsew")
        
        texto = "Abertura de conta PF"
        label_texto = customtkinter.CTkLabel(f2, text=texto)
        label_texto.pack()

        self.abertura.title('Cadastro de Cliente')

        label_nome = customtkinter.CTkLabel(self.abertura, text="Digite seu nome")
        label_nome.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_nome = customtkinter.CTkEntry(self.abertura, placeholder_text="Digite seu nome completo")
        self.entry_nome.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

        label_cpf = customtkinter.CTkLabel(self.abertura, text="Digite seu CPF")
        label_cpf.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_cpf = customtkinter.CTkEntry(self.abertura, placeholder_text="Digite seu CPF")
        self.entry_cpf.grid(row=2, column=1, sticky="nswe", padx=10, pady=10)

        label_endereco = customtkinter.CTkLabel(self.abertura, text="Digite seu Endereço")
        label_endereco.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_endereco = customtkinter.CTkEntry(self.abertura, placeholder_text="Digite seu Endereço")
        self.entry_endereco.grid(row=3, column=1, sticky="nswe", padx=10, pady=10)

        label_telefone = customtkinter.CTkLabel(self.abertura, text="Digite seu telefone")
        label_telefone.grid(row=4, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_telefone = customtkinter.CTkEntry(self.abertura, placeholder_text="Digite seu telefone")
        self.entry_telefone.grid(row=4, column=1, sticky="nswe", padx=10, pady=10)

        label_email = customtkinter.CTkLabel(self.abertura, text="Digite seu email")
        label_email.grid(row=5, column=0, sticky="nswe", padx=10, pady=10)
        self.entry_email = customtkinter.CTkEntry(self.abertura, placeholder_text="Digite seu email")
        self.entry_email.grid(row=5, column=1, sticky="nswe", padx=10, pady=10)

        # label_agencia = customtkinter.CTkLabel(self, text="Digite seu agencia")
        # label_agencia.grid(row=6, column=0, sticky="nswe", padx=10, pady=10)

        # self.agencia = customtkinter.CTkEntry(self, placeholder_text="Digite seu agencia")
        # self.agencia.grid(row=6, column=1, sticky="nswe", padx=10, pady=10)

        # label_conta = customtkinter.CTkLabel(self, text="Digite seu conta")
        # label_conta.grid(row=7, column=0, sticky="nswe", padx=10, pady=10)
        # self.conta = customtkinter.CTkEntry(self, placeholder_text="Digite seu conta")
        # self.conta.grid(row=7, column=1, sticky="nswe", padx=10, pady=10)

        # label_especial = customtkinter.CTkLabel(self, text="Cliente especial?")
        # label_especial.grid(row=8, column=0, sticky="nswe", padx=10, pady=10)
        self.enviar_dados = customtkinter.CTkButton(self.abertura, text="Salvar", command=self.cadastrar)
        self.enviar_dados.grid(row=9, column=0, columnspan=2, pady=10)
        
        

    def cadastrar(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        endereco = self.entry_endereco.get()
        telefone = self.entry_telefone.get()
        email = self.entry_email.get()
        
        cadastrar_cliente(self ,nome, cpf, endereco, telefone, email)

        


        # self.nome_var = tk.StringVar()
        # self.especial = customtkinter.CTkCheckBox(self.abertura, text="Sim", variable=self.nome_var)
        # self.especial.grid(row=8, column=1)


class AberturaPJ(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.abeturaPJ = customtkinter.CTkToplevel()
        self.abeturaPJ.geometry("600x500")
        self.abeturaPJ.grid_columnconfigure(1, weight=1)
        self.abeturaPJ.grid_rowconfigure(5, weight=0)

        f1 = customtkinter.CTkFrame(self.abeturaPJ, width=100, height=50)
        f2 = customtkinter.CTkFrame(self.abeturaPJ, width=100, height=50)
        f3 = customtkinter.CTkFrame(self.abeturaPJ, width=100, height=50)
        f1.grid(row=0, column=0, sticky="nsew")
        f2.grid(row=0, column=1, sticky="nsew")
        f3.grid(row=0, column=2, sticky="nsew")
        texto = "Abertura de conta PJ"
        label_texto = customtkinter.CTkLabel(f2, text=texto)

        texto = font.Font(size=20)
        label_texto.pack()

        self.abeturaPJ.title('Cadastro de Cliente PJ')

        label_nome = customtkinter.CTkLabel(self.abeturaPJ, text="Digite a Razão Social")
        label_nome.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.nome = customtkinter.CTkEntry(self.abeturaPJ, placeholder_text="Razão Social")
        self.nome.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

        label_cpf = customtkinter.CTkLabel(self.abeturaPJ, text="Digite o CNPJ")
        label_cpf.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.cpf = customtkinter.CTkEntry(self.abeturaPJ, placeholder_text="CNPJ")
        self.cpf.grid(row=2, column=1, sticky="nswe", padx=10, pady=10)

        label_endereco = customtkinter.CTkLabel(self.abeturaPJ, text="Digite o Endereço")
        label_endereco.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
        self.endereco = customtkinter.CTkEntry(self.abeturaPJ, placeholder_text="Endereço")
        self.endereco.grid(row=3, column=1, sticky="nswe", padx=10, pady=10)

        label_telefone = customtkinter.CTkLabel(self.abeturaPJ, text="Digite o telefone")
        label_telefone.grid(row=4, column=0, sticky="nswe", padx=10, pady=10)
        self.telefone = customtkinter.CTkEntry(self.abeturaPJ, placeholder_text="telefone")
        self.telefone.grid(row=4, column=1, sticky="nswe", padx=10, pady=10)

        label_email = customtkinter.CTkLabel(self.abeturaPJ, text="Digite o email da Empresa")
        label_email.grid(row=5, column=0, sticky="nswe", padx=10, pady=10)
        self.email = customtkinter.CTkEntry(self.abeturaPJ, placeholder_text="Email")
        self.email.grid(row=5, column=1, sticky="nswe", padx=10, pady=10)

        label_agencia = customtkinter.CTkLabel(self.abeturaPJ, text="Digite a Agencia")
        label_agencia.grid(row=6, column=0, sticky="nswe", padx=10, pady=10)
        self.agencia = customtkinter.CTkEntry(self.abeturaPJ, placeholder_text="agencia")
        self.agencia.grid(row=6, column=1, sticky="nswe", padx=10, pady=10)

        label_conta = customtkinter.CTkLabel(self.abeturaPJ, text="Digite a conta")
        label_conta.grid(row=7, column=0, sticky="nswe", padx=10, pady=10)
        self.conta = customtkinter.CTkEntry(self.abeturaPJ, placeholder_text="conta")
        self.conta.grid(row=7, column=1, sticky="nswe", padx=10, pady=10)

        label_especial = customtkinter.CTkLabel(self.abeturaPJ, text="Cliente especial ?")
        label_especial.grid(row=8, column=0, sticky="nswe", padx=10, pady=10)

        self.enviar_dados = customtkinter.CTkButton(self.abeturaPJ, text="Salvar")
        self.enviar_dados.grid(row=9, column=0, columnspan=2, pady=10)

        self.nome_var = tk.StringVar()
        self.especial = customtkinter.CTkCheckBox(self.abeturaPJ, text="Sim", variable=self.nome_var)
        self.especial.grid(row=8, column=1)

class Alteraçao(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(5, weight=0)

        f1 = customtkinter.CTkFrame(self, width=100, height=50)
        f2 = customtkinter.CTkFrame(self, width=100, height=50)
        f3 = customtkinter.CTkFrame(self, width=100, height=50)
        f1.grid(row=0, column=0, sticky="nsew")
        f2.grid(row=0, column=1, sticky="nsew")
        f3.grid(row=0, column=2, sticky="nsew")

        texto = "Alteração de dados do cliente"
        label_texto = customtkinter.CTkLabel(f2, text=texto)
        texto = font.Font(size=20)
        label_texto.pack()

        self.title('Alteração de Cliente')

        label_nome = customtkinter.CTkLabel(self, text="Digite o CPF ou CNPJ")
        label_nome.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)

        nome = customtkinter.CTkEntry(self, placeholder_text="CPF ou CNPJ")
        nome.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

        alterar_dados = customtkinter.CTkButton(self, text="Alterar")
        alterar_dados.grid(row=9, column=0, columnspan=2, pady=10)


class CadastroBanco:
    def __init__(self):
        self.alteracao = customtkinter.CTkToplevel()
        self.alteracao.geometry("600x500")
        self.alteracao.grid_columnconfigure(1, weight=1)
        self.alteracao.grid_rowconfigure(5, weight=0)

        f1 = customtkinter.CTkFrame(self.alteracao, width=100, height=50)
        f2 = customtkinter.CTkFrame(self.alteracao, width=100, height=50)
        f3 = customtkinter.CTkFrame(self.alteracao, width=100, height=50)
        f1.grid(row=0, column=0, sticky="nsew")
        f2.grid(row=0, column=1, sticky="nsew")
        f3.grid(row=0, column=2, sticky="nsew")
        
        texto = "Cadastro de banco e Agencia e Gerente"
        label_texto = customtkinter.CTkLabel(f2, text=texto)
        label_texto.pack()

        self.alteracao.title('Cadastro de banco e Agencia e Gerente')

        label_nome_banco = customtkinter.CTkLabel(self.alteracao, text="Digite o nome do banco")
        label_nome_banco.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.banco = customtkinter.CTkEntry(self.alteracao, placeholder_text="Nome")
        self.banco.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

        label_ag = customtkinter.CTkLabel(self.alteracao, text="Digite o Numero da agencia")
        label_ag.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.agencia = customtkinter.CTkEntry(self.alteracao, placeholder_text="Numero")
        self.agencia.grid(row=2, column=1, sticky="nswe", padx=10, pady=10)

        label_gerente = customtkinter.CTkLabel(self.alteracao, text="Digite o nome do gerente")
        label_gerente.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
        self.gerente = customtkinter.CTkEntry(self.alteracao, placeholder_text="Nome Completo")
        self.gerente.grid(row=3, column=1, sticky="nswe", padx=10, pady=10)

        salvar_dados = customtkinter.CTkButton(self.alteracao, text="Salvar")
        salvar_dados.grid(row=9, column=0, columnspan=2, pady=10)
  
class MovimentaBancaria(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(5, weight=0)

        f1 = customtkinter.CTkFrame(self, width=100, height=50)
        f2 = customtkinter.CTkFrame(self, width=100, height=50)
        f3 = customtkinter.CTkFrame(self, width=100, height=50)
        f1.grid(row=0, column=0, sticky="nsew")
        f2.grid(row=0, column=1, sticky="nsew")
        f3.grid(row=0, column=2, sticky="nsew")

        texto = "Movimentação Bancária"
        label_texto = customtkinter.CTkLabel(f2, text=texto)
        texto = font.Font(size=20)
        label_texto.pack()

        self.title('Movimentação Bancária')

        label_nome_banco = customtkinter.CTkLabel(self, text="Digite o CPF ou CNPJ do cliente")
        label_nome_banco.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)

        banco = customtkinter.CTkEntry(self, placeholder_text="CPF ou CNPJ")
        banco.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

        alterar_dados = customtkinter.CTkButton(self, text="Salvar")
        alterar_dados.grid(row=9, column=0, columnspan=2, pady=10)

    
class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        self.grid_columnconfigure((0, 1), weight=2)
        self.geometry("600x500")
        texto_banco = customtkinter.CTkLabel(self, text="Sistema Bancario do Desenvolvedor")
        texto_banco.grid(row=2, column=1, padx=20, pady=20)


        abertura_pf = customtkinter.CTkButton(self, text="Abertura de Conta PF", command=CadastroCliente)
        abertura_pf.grid(row=2, column=0, padx=20, pady=20)


        abertura_pj = customtkinter.CTkButton(self, text="Abertura de Conta Pj",command=AberturaPJ)
        abertura_pj.grid(row=3, column=0, padx=20, pady=20)


        alteracao_conta = customtkinter.CTkButton(self, text="Alteração de conta",command=Alteraçao)
        alteracao_conta.grid(row=4, column=0, padx=20, pady=20)


        cadastro_banco = customtkinter.CTkButton(self, text="Cadastro de Banco",command=CadastroBanco)
        cadastro_banco.grid(row=5, column=0, padx=20, pady=20)


        servico_conta = customtkinter.CTkButton(self, text="Serviços de Conta", command=MovimentaBancaria)
        servico_conta.grid(row=6, column=0, padx=20, pady=20)
        
        self.toplevel_window = None
       




# App.title("Sistema Bancario do Desenvolvedor")
app = App()


app.mainloop()