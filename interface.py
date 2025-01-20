import customtkinter as ctk
from tkinter import filedialog ,StringVar

# Inicialização da interface
ctk.set_appearance_mode("dark")  # Define o modo de aparência (claro ou escuro)
ctk.set_default_color_theme("green")  # Define o tema de cores padrão

app = ctk.CTk()
app.geometry("400x300")
app.title("Minha Interface")

# Criando os elementos da interface
def selecionar_arquivo():
    
   
        # Abrir um diálogo para selecionar o arquivo
        caminho = filedialog.askopenfilename(title="Selecione um arquivo")
        if caminho:  # Verifica se algum arquivo foi selecionado
            arquivo.set(caminho)  # Atualiza a variável do campo "arquivo"
        desc = descricao.get()  # Obtém o texto do campo "descrição"
        print(desc, caminho)  # Passa os valores para a função externa
def publicar():
      
descricao = StringVar()
arquivo = StringVar()

label_descricao1 = ctk.CTkLabel(master=app, text="texto descritivo:").place(x=60, y=90)

entry_campo1 = ctk.CTkEntry(master=app, textvariable=descricao).place(x=60, y=120)

label_diretorio = ctk.CTkLabel(master=app, text="Diretorio:").place(x=60,y=150)

entry_diretorio = ctk.CTkEntry(master=app, textvariable=arquivo).place(x=60,y=180)


# ... outros campos de descrição e entry ...

# Botão para buscar diretório


    
botao_diretorio = ctk.CTkButton(master=app, text="Imagem", command=selecionar_arquivo)
botao_diretorio.place(x=200,y=180)
botao_publicar = ctk.CTkButton(master=app, text="Publicar", command=publicar)
botao_diretorio.place(x=200,y=180)


app.mainloop()