import customtkinter
from tkinter import * 
from cliente import *
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

app = customtkinter.CTk()  
app.grid_columnconfigure((0, 1), weight=2)
app.geometry("600x500")



def abrir_abertura():
    
    abertura = customtkinter.CTkToplevel()
    abertura.geometry("600x500")
    abertura.grid_columnconfigure(1, weight=1)
    abertura.grid_rowconfigure(5 , weight=0)
    

    f1=customtkinter.CTkFrame(abertura, width=100, height=50)
    f2=customtkinter.CTkFrame(abertura, width=100, height=50)
    f3=customtkinter.CTkFrame(abertura, width=100, height=50)
    f1.grid(row=0, column=0, sticky="nsew")
    f2.grid(row=0, column=1, sticky="nsew")
    f3.grid(row=0, column=2, sticky="nsew")
    texto = "Abertura de conta PF"
    label_texto = customtkinter.CTkLabel(f2, text=texto)
    
    texto = font.Font(size=20)  

    label_texto.pack()
                

    abertura.title('Cadastro de Cliente')

    label_nome=customtkinter.CTkLabel(abertura, text= "Digite seu nome")
    label_nome.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
    
    nome = customtkinter.CTkEntry(abertura, placeholder_text= "Digite seu nome completo")
    nome.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)
    
    label_cpf=customtkinter.CTkLabel(abertura, text= "Digite seu CPF")
    label_cpf.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
    
    cpf = customtkinter.CTkEntry(abertura, placeholder_text= "Digite seu CPF",)
    cpf.grid(row=2, column=1, sticky="nswe", padx=10, pady=10)

    label_endereco=customtkinter.CTkLabel(abertura, text= "Digite seu Endereço")
    label_endereco.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
    
    endereco = customtkinter.CTkEntry(abertura, placeholder_text= "Digite seu Endereço")
    endereco.grid(row=3, column=1, sticky="nswe", padx=10, pady=10)

    label_telefone=customtkinter.CTkLabel(abertura, text= "Digite seu telefone")
    label_telefone.grid(row=4, column=0, sticky="nswe", padx=10, pady=10)
    
    telefone = customtkinter.CTkEntry(abertura, placeholder_text= "Digite seu telefone" )
    telefone.grid(row=4, column=1, sticky="nswe", padx=10, pady=10)

    label_email=customtkinter.CTkLabel(abertura, text= "Digite seu email")
    label_email.grid(row=5, column=0, sticky="nswe", padx=10, pady=10)
    
    email = customtkinter.CTkEntry(abertura, placeholder_text= "Digite seu email")
    email.grid(row=5, column=1, sticky="nswe", padx=10, pady=10)

    label_agencia=customtkinter.CTkLabel(abertura, text= "Digite seu agencia")
    label_agencia.grid(row=6, column=0, sticky="nswe", padx=10, pady=10)
    
    agencia = customtkinter.CTkEntry(abertura, placeholder_text= "Digite seu agencia" )
    agencia.grid(row=6, column=1, sticky="nswe", padx=10, pady=10)

    label_conta=customtkinter.CTkLabel(abertura, text= "Digite seu conta")
    label_conta.grid(row=7, column=0, sticky="nswe", padx=10, pady=10)
    
    conta = customtkinter.CTkEntry(abertura, placeholder_text= "Digite seu conta")
    conta.grid(row=7, column=1, sticky="nswe", padx=10, pady=10)

    label_especial=customtkinter.CTkLabel(abertura, text= "Cliente especial ?")
    label_especial.grid(row=8, column=0, sticky="nswe", padx=10, pady=10)

    enviar_dados =customtkinter.CTkButton(abertura, text="Salvar")
    enviar_dados.grid(row=9, column=0, columnspan=2, pady=10)
    
    nome_var = tk.StringVar()
    especial = customtkinter.CTkCheckBox(abertura, text="Sim",variable=nome_var)
    especial.grid(row=8, column=1)


def abrir_aberturaPJ():
    
    abeturaPJ = customtkinter.CTkToplevel()
    abeturaPJ.geometry("600x500")
    abeturaPJ.grid_columnconfigure(1, weight=1)
    abeturaPJ.grid_rowconfigure(5 , weight=0)
    

    f1=customtkinter.CTkFrame(abeturaPJ, width=100, height=50)
    f2=customtkinter.CTkFrame(abeturaPJ, width=100, height=50)
    f3=customtkinter.CTkFrame(abeturaPJ, width=100, height=50)
    f1.grid(row=0, column=0, sticky="nsew")
    f2.grid(row=0, column=1, sticky="nsew")
    f3.grid(row=0, column=2, sticky="nsew")
    texto = "Abertura de conta PJ"
    label_texto = customtkinter.CTkLabel(f2, text=texto)
    
    texto = font.Font(size=20)  

    label_texto.pack()
                

    abeturaPJ.title('Cadastro de Cliente PJ')

    label_nome=customtkinter.CTkLabel(abeturaPJ, text= "Digite a Razão Social")
    label_nome.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
    
    nome = customtkinter.CTkEntry(abeturaPJ, placeholder_text= "Razão Social")
    nome.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)
    
    label_cpf=customtkinter.CTkLabel(abeturaPJ, text= "Digite o CNPJ")
    label_cpf.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
    
    cpf = customtkinter.CTkEntry(abeturaPJ, placeholder_text= "CNPJ",)
    cpf.grid(row=2, column=1, sticky="nswe", padx=10, pady=10)

    label_endereco=customtkinter.CTkLabel(abeturaPJ, text= "Digite o Endereço")
    label_endereco.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
    
    endereco = customtkinter.CTkEntry(abeturaPJ, placeholder_text= "Endereço")
    endereco.grid(row=3, column=1, sticky="nswe", padx=10, pady=10)

    label_telefone=customtkinter.CTkLabel(abeturaPJ, text= "Digite o telefone")
    label_telefone.grid(row=4, column=0, sticky="nswe", padx=10, pady=10)
    
    telefone = customtkinter.CTkEntry(abeturaPJ, placeholder_text= "telefone" )
    telefone.grid(row=4, column=1, sticky="nswe", padx=10, pady=10)

    label_email=customtkinter.CTkLabel(abeturaPJ, text= "Digite o email da Empresa")
    label_email.grid(row=5, column=0, sticky="nswe", padx=10, pady=10)
    
    email = customtkinter.CTkEntry(abeturaPJ, placeholder_text= "Email")
    email.grid(row=5, column=1, sticky="nswe", padx=10, pady=10)

    label_agencia=customtkinter.CTkLabel(abeturaPJ, text= "Digite a Agencia")
    label_agencia.grid(row=6, column=0, sticky="nswe", padx=10, pady=10)
    
    agencia = customtkinter.CTkEntry(abeturaPJ, placeholder_text= "agencia" )
    agencia.grid(row=6, column=1, sticky="nswe", padx=10, pady=10)

    label_conta=customtkinter.CTkLabel(abeturaPJ, text= "Digite a conta")
    label_conta.grid(row=7, column=0, sticky="nswe", padx=10, pady=10)
    
    conta = customtkinter.CTkEntry(abeturaPJ, placeholder_text= "conta")
    conta.grid(row=7, column=1, sticky="nswe", padx=10, pady=10)

    label_especial=customtkinter.CTkLabel(abeturaPJ, text= "Cliente especial ?")
    label_especial.grid(row=8, column=0, sticky="nswe", padx=10, pady=10)

    enviar_dados =customtkinter.CTkButton(abeturaPJ, text="Salvar")
    enviar_dados.grid(row=9, column=0, columnspan=2, pady=10)
    
    nome_var = tk.StringVar()
    especial = customtkinter.CTkCheckBox(abeturaPJ, text="Sim",variable=nome_var)
    especial.grid(row=8, column=1)


def abrir_alteraçao():
    
    alte_cli = customtkinter.CTkToplevel()
    alte_cli.geometry("600x500")
    alte_cli.grid_columnconfigure(1, weight=1)
    alte_cli.grid_rowconfigure(5 , weight=0)
    

    f1=customtkinter.CTkFrame(alte_cli, width=100, height=50)
    f2=customtkinter.CTkFrame(alte_cli, width=100, height=50)
    f3=customtkinter.CTkFrame(alte_cli, width=100, height=50)
    f1.grid(row=0, column=0, sticky="nsew")
    f2.grid(row=0, column=1, sticky="nsew")
    f3.grid(row=0, column=2, sticky="nsew")
    texto = "Alteraçao de dados do cliente"
    label_texto = customtkinter.CTkLabel(f2, text=texto)
    
    texto = font.Font(size=20)  

    label_texto.pack()
                

    alte_cli.title('Alteração de Cliente')

    label_nome=customtkinter.CTkLabel(alte_cli, text= "Digite o CPF ou CPNJ")
    label_nome.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
    
    nome = customtkinter.CTkEntry(alte_cli, placeholder_text= "CPF ou CPNJ")
    nome.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)
    

    alterar_dados =customtkinter.CTkButton(alte_cli, text="Alterar")
    alterar_dados.grid(row=9, column=0, columnspan=2, pady=10)

def cad_banco():
    
    alteraçao = customtkinter.CTkToplevel()
    alteraçao.geometry("600x500")
    alteraçao.grid_columnconfigure(1, weight=1)
    alteraçao.grid_rowconfigure(5 , weight=0)
    

    f1=customtkinter.CTkFrame(alteraçao, width=100, height=50)
    f2=customtkinter.CTkFrame(alteraçao, width=100, height=50)
    f3=customtkinter.CTkFrame(alteraçao, width=100, height=50)
    f1.grid(row=0, column=0, sticky="nsew")
    f2.grid(row=0, column=1, sticky="nsew")
    f3.grid(row=0, column=2, sticky="nsew")
    texto = "Cadastro de banco e Agencia e Gerente"
    label_texto = customtkinter.CTkLabel(f2, text=texto)
    
    texto = font.Font(size=20)  

    label_texto.pack()
                

    alteraçao.title('Cadastro de banco e Agencia e Gerente')

    label_nome_banco=customtkinter.CTkLabel(alteraçao, text= "Digite o nome do banco")
    label_nome_banco.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
    
    banco = customtkinter.CTkEntry(alteraçao, placeholder_text= "Nome")
    banco.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

    label_ag=customtkinter.CTkLabel(alteraçao, text= "Digite o Numero da agencia")
    label_ag.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
    
    agencia= customtkinter.CTkEntry(alteraçao, placeholder_text= "Numero")
    agencia.grid(row=2, column=1, sticky="nswe", padx=10, pady=10)

    label_ag=customtkinter.CTkLabel(alteraçao, text= "Digite o nome do gerente")
    label_ag.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
    
    agencia= customtkinter.CTkEntry(alteraçao, placeholder_text= "Nome Completo")
    agencia.grid(row=3, column=1, sticky="nswe", padx=10, pady=10)
    

    alterar_dados =customtkinter.CTkButton(alteraçao, text="salvar")
    alterar_dados.grid(row=9, column=0, columnspan=2, pady=10)
    
def movimenta():
    
    mov_conta = customtkinter.CTkToplevel()
    mov_conta.geometry("600x500")
    mov_conta.grid_columnconfigure(1, weight=1)
    mov_conta.grid_rowconfigure(5 , weight=0)
    

    f1=customtkinter.CTkFrame(mov_conta, width=100, height=50)
    f2=customtkinter.CTkFrame(mov_conta, width=100, height=50)
    f3=customtkinter.CTkFrame(mov_conta, width=100, height=50)
    f1.grid(row=0, column=0, sticky="nsew")
    f2.grid(row=0, column=1, sticky="nsew")
    f3.grid(row=0, column=2, sticky="nsew")
    texto = "Movimentaçao Bancaria"
    label_texto = customtkinter.CTkLabel(f2, text=texto)
    
    texto = font.Font(size=20)  

    label_texto.pack()
                

    mov_conta.title('Movimentação Bancaria')

    label_nome_banco=customtkinter.CTkLabel(mov_conta, text= "Digite o CPF ou CNPJ do cliente")
    label_nome_banco.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
    
    banco = customtkinter.CTkEntry(mov_conta, placeholder_text= "cpf")
    banco.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

    
    

    alterar_dados =customtkinter.CTkButton(mov_conta, text="salvar")
    alterar_dados.grid(row=9, column=0, columnspan=2, pady=10)
    


texto_banco = customtkinter.CTkLabel(master=app, text="Sistema Bancario do Desenvolvedor")
texto_banco.grid(row=2, column=1, padx=20, pady=20)


abertura_pf = customtkinter.CTkButton(master=app, text="Abertura de Conta PF", command=abrir_abertura)
abertura_pf.grid(row=2, column=0, padx=20, pady=20)


abertura_pj = customtkinter.CTkButton(master=app, text="Abertura de Conta Pj",command=abrir_aberturaPJ )
abertura_pj.grid(row=3, column=0, padx=20, pady=20)


alteracao_conta = customtkinter.CTkButton(master=app, text="Alteração de conta",command=abrir_alteraçao)
alteracao_conta.grid(row=4, column=0, padx=20, pady=20)


cadastro_banco = customtkinter.CTkButton(master=app, text="Cadastro de Banco",command=cad_banco)
cadastro_banco.grid(row=5, column=0, padx=20, pady=20)


servico_conta = customtkinter.CTkButton(master=app, text="Serviços de Conta", command=movimenta)
servico_conta.grid(row=6, column=0, padx=20, pady=20)





app.title("Sistema Bancario do Desenvolvedor")



app.mainloop()