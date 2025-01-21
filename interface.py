import customtkinter as ctk
from tkinter import filedialog ,StringVar
import automacao_linkedin as auto


# Inicialização da interface
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("green")  


app = ctk.CTk()
app.geometry("550x300")
app.title("Minha Interface")


# buscando os arquivos
def selecionar_arquivo():
    caminho = filedialog.askopenfilename(title="Selecione um arquivo")# Abrir um diálogo para selecionar o arquivo
    if caminho:  
        arquivo.set(caminho)  # Atualiza a variável do campo "arquivo"
   

#iniciando a publicação        
def publicar():
    desc =  entry_campo1.get("1.0", "end") # Obtém o texto do campo "descrição"
    caminho = arquivo.get()
    barra_final_indice = caminho.rfind('/')#pega o indice da ultima barra
    caminho_formatado = caminho[barra_final_indice +1 :]#fatia a partir  do indice da ultima barra
    print(f"publicado {desc,caminho_formatado}")

    auto.automatizar(desc, caminho_formatado)


arquivo = StringVar()

label_title =ctk.CTkLabel(master=app, text='ATUALIZAÇÕES AUTOMATIZADAS-LINKEDIN',font=('Ariel bold',20)).place(x=60,y=40)

label_descricao1 = ctk.CTkLabel(master=app, text="texto descritivo:").place(x=60, y=90)

entry_campo1 = ctk.CTkTextbox(master=app, width=420, height=70)
entry_campo1.place(x=60, y=120) 

label_diretorio = ctk.CTkLabel(master=app, text="Diretorio:").place(x=60,y=190)

entry_diretorio = ctk.CTkEntry(master=app, textvariable=arquivo, width=350).place(x=60,y=220)
  
botao_diretorio = ctk.CTkButton(master=app, text="Imagem", width=60, command=selecionar_arquivo)
botao_diretorio.place(x=420,y=220)

botao_publicar = ctk.CTkButton(master=app, text="Publicar", command=publicar)
botao_publicar.place(x=200,y=260)


app.mainloop()