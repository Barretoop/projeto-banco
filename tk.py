import customtkinter
from tkinter import * 
from cliente import *
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

app = customtkinter.CTk()  
app.grid_columnconfigure((0, 1), weight=2)
app.geometry("600x500")



def abrir_abertura():
    
    abertura = customtkinter.CTkToplevel(app)
    abertura.geometry("600x500")
    abertura.grid_columnconfigure(0, weight=1)
    abertura.grid_rowconfigure(1, weight=0)
    # Label_middle = customtkinter.CTkLabel(abertura, text ='Cadastro de Cliente')
    # Label_middle.place(relx=0.017, rely=0.0, relheight=0.122, relwidth=0.983)
    

    f1=customtkinter.CTkFrame(abertura, width=5, height=50)
    f1.grid(row=0, column=0, sticky="nsew")

    
                

    abertura.title('Cadastro de Cliente')

    # tela=customtkinter.CTkLabel(abertura, text= "Cadastro De Cliente")
    # tela.grid(row=1, column=0)

    label_nome=customtkinter.CTkLabel(abertura, text= "Digite seu nome")
    label_nome.grid(row=5, column=0)
    
    nome = customtkinter.CTkEntry(abertura, placeholder_text= "Digite seu nome completo")
    nome.grid(row=6, column=0)

    # label_cpf=customtkinter.CTkLabel(abertura, text= "Digite seu CPF")
    # label_cpf.grid(row=4, column=0)
    
    # cpf = customtkinter.CTkEntry(abertura, placeholder_text= "Digite seu CPF",)
    # cpf.grid(row=5, column=0)

    # label_endereco=customtkinter.CTkLabel(abertura, text= "Digite seu Endereço")
    # label_endereco.grid(row=6, column=0)
    
    # endereco = customtkinter.CTkEntry(abertura, placeholder_text= "Digite seu Endereço")
    # endereco.grid(row=7, column=0)

    # label_telefone=customtkinter.CTkLabel(abertura, text= "Digite seu telefone")
    # label_telefone.grid(row=8, column=0)
    
    # telefone = customtkinter.CTkEntry(abertura, placeholder_text= "Digite seu telefone" )
    # telefone.grid(row=9, column=0)

    # label_email=customtkinter.CTkLabel(abertura, text= "Digite seu email")
    # label_email.grid(row=1, column=0)
    
    # email = customtkinter.CTkEntry(abertura, placeholder_text= "Digite seu email")
    # email.grid(row=2, column=1)

    # label_agencia=customtkinter.CTkLabel(abertura, text= "Digite seu agencia")
    # label_agencia.grid(row=3, column=1)
    
    # agencia = customtkinter.CTkEntry(abertura, placeholder_text= "Digite seu agencia" )
    # agencia.grid(row=4, column=1)

    # label_conta=customtkinter.CTkLabel(abertura, text= "Digite seu conta")
    # label_conta.grid(row=5, column=1)
    
    # conta = customtkinter.CTkEntry(abertura, placeholder_text= "Digite seu conta")
    # conta.grid(row=6, column=1)

    # label_especial=customtkinter.CTkLabel(abertura, text= "Cliente especial ?")
    # label_especial.grid(row=7, column=1)
    
    # especial = customtkinter.CTkCheckBox(abertura, placeholder_text= "Digite seu especial", type=NUMERIC)
    # especial.grid(row=2, column=0)








texto_banco = customtkinter.CTkLabel(master=app, text="Sistema Bancario do Desenvolvedor")
texto_banco.grid(row=2, column=1, padx=20, pady=20)


abertura_pf = customtkinter.CTkButton(master=app, text="Abertura de Conta PF", command=abrir_abertura)
abertura_pf.grid(row=2, column=0, padx=20, pady=20)


abertura_pj = customtkinter.CTkButton(master=app, text="Abertura de Conta Pj" )
abertura_pj.grid(row=3, column=0, padx=20, pady=20)


alteracao_conta = customtkinter.CTkButton(master=app, text="Alteração de conta")
alteracao_conta.grid(row=4, column=0, padx=20, pady=20)


cadastro_banco = customtkinter.CTkButton(master=app, text="Cadastro de Banco")
cadastro_banco.grid(row=5, column=0, padx=20, pady=20)


servico_conta = customtkinter.CTkButton(master=app, text="Serviços de Conta")
servico_conta.grid(row=6, column=0, padx=20, pady=20)




app.title("Sistema Bancario do Desenvolvedor")



app.mainloop()