import customtkinter as ctk
from tkinter import ttk, messagebox
from view import *
from tkcalendar import DateEntry
import time
import threading


# inserindo dados na tabela
app = ctk.CTk() # Inicia a Janela
app._set_appearance_mode("dark")
app.title("Sitema de Alerta") # Titulo do App
app.geometry('1043x453') # Tamanho da Janela
app.resizable(False,False) # bloqueando o ajuste de tela
app.iconbitmap("Imagens/Navas.ico") # Icone


######################## Fontes #######################
font_titulo = ctk.CTkFont(family='Ivy', size=17)
font_button = ctk.CTkFont(family='Ivy', size=15)
font_buttonc = ctk.CTkFont(family='Ivy',size=5)


########################  Dividindo a Tela  #######################
frame_cima = ctk.CTkFrame(app,width=310, height=50)
frame_cima.grid(row=0,column=0,pady=0,sticky='nsew')

frame_baixo = ctk.CTkFrame(app,width=310, height=403)
frame_baixo.grid(row=1,column=0,pady=0,sticky='nsew')

frame_direita = ctk.CTkFrame(app,width=588, height=403)
frame_direita.grid(row=0,column=1,rowspan=2,padx=1,pady=0, sticky='nsew')



########################  Label Cima  #######################
titulo_cima = ctk.CTkLabel(frame_cima,text='Formulario de cobrança', font=font_titulo)
titulo_cima.place(x=10,y=10)

def consulta_p():
    time.sleep(2)
    consulta_prazos()

def mostrar():
    

    global tree

    lista = mostrar_info()
    list_topo = ['','FORNECEDOR','NF','DATA REGISTRADA ','STATUS']

    tree = ttk.Treeview(frame_direita,selectmode="extended",columns=list_topo, show="headings")

    #vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita,orient="vertical",command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(frame_direita,orient="horizontal",command=tree.xview)

    tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)

    tree.grid(column=0, row=0,sticky='nsew')
    vsb.grid(column=1, row=0,sticky='ns')
    hsb.grid(column=0,row=1,sticky='ew')
    frame_direita.grid_rowconfigure(0,weight=12)

    hd=["center","nw","center","nw","nw","center"]
    h=[0,300,100,150,160,50]
    n=0
    

    for col in list_topo:
        tree.heading(col, text=col.title(), anchor='center')
        tree.column(col,width=h[n],anchor=hd[n])
        n+=1
    for item in lista:
        tree.insert('','end', values=item)

       




def insert():
    # Pegando as informações das Entry
    fornecedor = e_fornecedor.get()
    nf = e_nf.get()
    data = e_data.get()
    status = e_status.get()

    lista = [fornecedor, nf, data, status]
    
    if fornecedor== '':
        messagebox.showerror('Erro','O Fornecedor nao foi preenchido')
    else:
        inserir_info(lista)
        # Mostrando as informações na Tela do usuario
        mostrar()
        messagebox.showinfo("Sucesso","Dados inseridos com sucesso")
        # deletando as informações das Entry
        e_fornecedor.delete(0, 'end')
        e_nf.delete(0, 'end')
        e_data.delete(0, 'end')
        e_status.set("SELECIONE")

    for widget in frame_direita.winfo_children():
        widget.destroy()
        mostrar()
        

mostrar()
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        # deletando as informações das Entry de precaução
        e_fornecedor.delete(0, 'end')
        e_nf.delete(0, 'end')
        e_status.set("SELECIONE")
        e_data.delete(0,'end')
        
        e_fornecedor.insert(0, treev_lista[1])
        e_nf.insert(0, treev_lista[2])
        e_data.insert(0,treev_lista[3])
        
        def update():
            #pegando as informações que foram atualizadas das Entry
            fornecedor = e_fornecedor.get()
            nf = e_nf.get()
            status = e_status.get()
            data = e_data.get()
            
            lista_atualizar = [fornecedor, nf, data, status, valor]
            if e_fornecedor.get()=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                
            else:
                atualizar_form(lista_atualizar)
                button_confirmar.destroy()
                messagebox.showinfo(
                    'Sucesso', 'Os dados foram atualizados com sucesso')
                mostrar()
                button_deletar.configure(state="enable",fg_color='red'),
                button_insert.configure(state="enable",fg_color='green'),
                button_atualizar.configure(state="enable",fg_color='blue')

                e_fornecedor.delete(0, 'end')
                e_nf.delete(0, 'end')
                e_data.delete(0, 'end')
            
        button_confirmar = ctk.CTkButton(frame_baixo,fg_color='green',text='Confirmar',width=100,height=10,font=font_button, command=update)
        button_confirmar.place(x=200, y=270)
########################  BOTÕES DISABLED  #######################
        button_deletar.configure(state="disabled")
        button_insert.configure(state="disabled")
        button_atualizar.configure(state="disabled")

    except IndexError:
            messagebox.showerror(
            'Erro', 'Seleciona um dos dados na tabela')
# funcao deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        
        deletar_form([valor])
        
        messagebox.showinfo(
            'Sucesso', 'Os dados foram deletados com sucesso')

        for widget in frame_direita.winfo_children():
            widget.destroy()

            e_fornecedor.delete(0, 'end')
            e_nf.delete(0, 'end')
            e_data.delete(0, 'end')

        mostrar()

    except IndexError:
        messagebox.showerror(
            'Erro', 'Seleciona um dos dados na tabela')    

########################  Configurando Frame Baixo  #######################

########################  FORNECEDOR  #######################
l_fornecedor = ctk.CTkLabel(frame_baixo,text='FORNECEDOR:', font=font_titulo)
l_fornecedor.place(x=10,y=10)
e_fornecedor = ctk.CTkEntry(frame_baixo,width=290,justify='left')
e_fornecedor.place(x=10,y=40)

########################  NF  #######################
l_nf = ctk.CTkLabel(frame_baixo,text='NF:', font=font_titulo)
l_nf.place(x=10,y=80)
e_nf = ctk.CTkEntry(frame_baixo,width=290,justify='left')
e_nf.place(x=10,y=110)

l_data = ctk.CTkLabel(frame_baixo, text='DATA:', font=font_titulo)
l_data.place(x=10,y=140)
e_data = DateEntry(frame_baixo,year=2024,width=44,fieldbackground='dark green',
                borderwidth=7,date_pattern='yyyy-MM-dd',
                arrowcolor='white')
e_data.place(x=10,y=170)

########################  STATUS  #######################
l_status = ctk.CTkLabel(frame_baixo,text='STATUS:', font=font_titulo)
l_status.place(x=10,y=210)
e_status = ctk.CTkComboBox(frame_baixo,width=290,justify='left',
                            values=["PENDENTE","CONFIRMADO"])
e_status.place(x=10,y=240)
e_status.set("SELECIONE")

########################  BOTÕES  #######################
button_insert = ctk.CTkButton(frame_baixo,fg_color='green',text='Inserir',width=130,font=font_button, command=insert)
button_insert.place(x=10,y=315)

button_atualizar = ctk.CTkButton(frame_baixo,fg_color='blue',text='Atualizar',width=130,font=font_button,command=atualizar)
button_atualizar.place(x=160,y=315)

button_deletar = ctk.CTkButton(frame_baixo,fg_color='red',text='Deletar',width=280,font=font_button, command=deletar)
button_deletar.place(x=10,y=360)

threading.Thread(target=consulta_p).start()
app.mainloop()