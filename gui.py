import customtkinter
import tkinter as tk
from tkinter import font
from clienteB import cadastrar_cliente
from clienteB import cadastrar_banco
from clienteB import buscar_cpf
from CTkMessagebox import CTkMessagebox
import sqlite3





class PjPf():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        msg = CTkMessagebox(title="Qual tipo de conta ?", message="Pessoa Fisica ou Juridica ?",  
                                icon="question",option_1="Cancelar", option_3="Fisica", option_2="Juridica")
        response = msg.get()
        if response =="Fisica":
           
           self.abrir_cadastro_cliente_PF()
        elif response == "Juridica":
            self._abrir_cadastro_cliente_Pj()
        else:
            msg.destroy()



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
        label_nome.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
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
        self.entry_bc.set("Selecione")
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
        self.entry_gen.set("Selecione")
        self.entry_gen.configure(values=gerente)

        conn = sqlite3.connect('clientes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT gerente FROM bancos ")
        resultados_gen = cursor.fetchall()
        for resultado_gen in resultados_gen:
            gerente.append(resultado_gen[0])
        self.entry_gen.configure(values=gerente)



        def atualizar_label():
                radio_var = radiobutton_1.get()
                if radio_var == "on":
                    slider.grid(row=10, column=1, sticky="nswe" )
                else:
                    slider.grid_forget()

        radio_var = customtkinter.StringVar(value="off")

        label_especial = customtkinter.CTkLabel(Cad_pf, text="Cliente especial escolha o valor do Limite?")
        label_especial.grid(row=9, column=0, sticky="nswe", padx=10, pady=10)
        radiobutton_1 = customtkinter.CTkSwitch(Cad_pf, text="Sim", variable=radio_var, onvalue="on", offvalue="off" ,command=atualizar_label)
        radiobutton_1.grid(row=9, column=1, sticky="nswe")
        print(radio_var.get())
        slider = customtkinter.CTkSlider(Cad_pf, from_=0, to=100 ,width=100,height=20 )

            
            
    def cadastrar(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        endereco = self.entry_endereco.get()
        telefone = self.entry_telefone.get()
        email = self.entry_email.get()
        conta = self.entry_conta.get()
        banco= self.entry_bc.get()
        gerente = self.entry_gen.get()

        
        cadastrar_cliente(self, nome, cpf, endereco, telefone, email, conta,banco,gerente)

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

        label_nome = customtkinter.CTkLabel(abeturaPJ, text="Digite a Razão Social")
        label_nome.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        nome = customtkinter.CTkEntry(abeturaPJ, placeholder_text="Razão Social")
        nome.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

        label_cpf = customtkinter.CTkLabel(abeturaPJ, text="Digite o CNPJ")
        label_cpf.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        cpf = customtkinter.CTkEntry(abeturaPJ, placeholder_text="CNPJ")
        cpf.grid(row=2, column=1, sticky="nswe", padx=10, pady=10)

        label_endereco = customtkinter.CTkLabel(abeturaPJ, text="Digite o Endereço")
        label_endereco.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
        endereco = customtkinter.CTkEntry(abeturaPJ, placeholder_text="Endereço")
        endereco.grid(row=3, column=1, sticky="nswe", padx=10, pady=10)

        label_telefone = customtkinter.CTkLabel(abeturaPJ, text="Digite o telefone")
        label_telefone.grid(row=4, column=0, sticky="nswe", padx=10, pady=10)
        telefone = customtkinter.CTkEntry(abeturaPJ, placeholder_text="telefone")
        telefone.grid(row=4, column=1, sticky="nswe", padx=10, pady=10)

        label_email = customtkinter.CTkLabel(abeturaPJ, text="Digite o email da Empresa")
        label_email.grid(row=5, column=0, sticky="nswe", padx=10, pady=10)
        email = customtkinter.CTkEntry(abeturaPJ, placeholder_text="Email")
        email.grid(row=5, column=1, sticky="nswe", padx=10, pady=10)

        label_agencia = customtkinter.CTkLabel(abeturaPJ, text="Digite a Agencia")
        label_agencia.grid(row=6, column=0, sticky="nswe", padx=10, pady=10)
        agencia = customtkinter.CTkEntry(abeturaPJ, placeholder_text="agencia")
        agencia.grid(row=6, column=1, sticky="nswe", padx=10, pady=10)

        label_conta = customtkinter.CTkLabel(abeturaPJ, text="Digite a conta")
        label_conta.grid(row=7, column=0, sticky="nswe", padx=10, pady=10)
        conta = customtkinter.CTkEntry(abeturaPJ, placeholder_text="conta")
        conta.grid(row=7, column=1, sticky="nswe", padx=10, pady=10)

        label_especial = customtkinter.CTkLabel(abeturaPJ, text="Cliente especial ?")
        label_especial.grid(row=8, column=0, sticky="nswe", padx=10, pady=10)

        enviar_dados = customtkinter.CTkButton(abeturaPJ, text="Salvar")
        enviar_dados.grid(row=9, column=0, columnspan=2, pady=10)

        # nome_var = tk.StringVar()
        # especial = customtkinter.CTkCheckBox(abeturaPJ, text="Sim", variable=nome_var)
        # self.especial.grid(row=8, column=1)



class Alteracao:
    def __init__(self):
        self.AltCliente=customtkinter.CTkToplevel()
        self.AltCliente.geometry("600x500")
        self.AltCliente.grid_columnconfigure(1, weight=1)
        self.AltCliente.grid_rowconfigure(5, weight=0)

        f1 = customtkinter.CTkFrame(self.AltCliente, width=100, height=50)
        f2 = customtkinter.CTkFrame(self.AltCliente, width=100, height=50)
        f3 = customtkinter.CTkFrame(self.AltCliente, width=100, height=50)
        f1.grid(row=0, column=0, sticky="nsew")
        f2.grid(row=0, column=1, sticky="nsew")
        f3.grid(row=0, column=2, sticky="nsew")

        texto = "Alteração de dados do cliente"
        label_texto = customtkinter.CTkLabel(f2, text=texto)
        texto = font.Font(size=20)
        label_texto.pack()

        self.AltCliente.title('Alteração de Cliente')

        label_nome = customtkinter.CTkLabel(self.AltCliente, text="Digite o CPF ou CNPJ")
        label_nome.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)

        self.entry_cpf = customtkinter.CTkEntry(self.AltCliente, placeholder_text="CPF ou CNPJ")
        self.entry_cpf.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

        busca_cpf = customtkinter.CTkButton(self.AltCliente, text="Alterar" ,command=self.buscarCPF)
        busca_cpf.grid(row=9, column=0, columnspan=2, pady=10)

    def buscarCPF(self):
        cpf = self.entry_cpf.get()
        


        buscar_cpf(self,cpf)















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

    def cadastrarBanco(self):
        banco = self.entry_banco.get()
        agencia = self.entry_agencia.get()
        gerente = self.entry_gerente.get()

    
        cadastrar_banco(self,banco,agencia,gerente)
  
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
    def __init__(self,master=None):
        super().__init__(master)  
        self.grid_columnconfigure((0, 1), weight=2)
        self.geometry("600x500")
        customtkinter.set_appearance_mode("dark")
       
        texto_banco = customtkinter.CTkLabel(self, text="Sistema Bancario do Desenvolvedor")
        texto_banco.grid(row=2, column=1, padx=20, pady=20)
        self.title("Sistema Bancario do Desenvolvedor")


        abertura_pf = customtkinter.CTkButton(self, text="Abertura de Conta PF/PJ", command=PjPf)
        abertura_pf.grid(row=2, column=0, padx=20, pady=20)


        alteracao_conta = customtkinter.CTkButton(self, text="Alteração de conta",command=Alteracao)
        alteracao_conta.grid(row=4, column=0, padx=20, pady=20)


        cadastro_banco = customtkinter.CTkButton(self, text="Cadastro de Banco",command=CadastroBanco)
        cadastro_banco.grid(row=5, column=0, padx=20, pady=20)


        servico_conta = customtkinter.CTkButton(self, text="Serviços de conta", command=MovimentaBancaria)
        servico_conta.grid(row=6, column=0, padx=20, pady=20)
        
        self.toplevel_window = None
        
        

app = App()
app.mainloop()