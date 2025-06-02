from tkinter import *
from tkinter import ttk, messagebox,filedialog
import time
from datetime import date
import pymysql

def Sair():
    Janela2.destroy()

#def ExportarDados():
#    url = filedialog.asksaveasfilename(defaultextension='.csv')
#    indexing = Topicos.get_children()
#    novaLista = ()
#    for index in indexing:
#        conteudo = Topicos.item(index)
#        ListaDeDados = conteudo['values']
#        novaLista.append(ListaDeDados)
        

def AtualizarCliente():
    def AtualizarDadosCliente():
        Query = 'update alldata set nome=%s,telefone=%s,endereço=%s,email=%s,compra=%s,formapagamento=%s,data=%s,horario=%s where cpf=%s'
        meuCursor.execute(Query,(NomeEntry.get(),TelefoneEntry.get(),EndereçoEntry.get(),
                                    EmailEntry.get(), CompraEntry.get(),FPEntry.get(),data,horario,CpfEntry.get()))
        con.commit()
        messagebox.showinfo('Sucesso', 'Os dados do cliente foram atualizados.')
        JanelaAtualizarCliente.destroy()
        ListarCliente()
    
    JanelaAtualizarCliente = Toplevel()
    JanelaAtualizarCliente.title('Atualizar Cliente')
    JanelaAtualizarCliente.resizable(False,False)
    JanelaAtualizarCliente.grab_set()
    
    CpfLabel = Label(JanelaAtualizarCliente, text='Cpf:', font=('trebuchet ms',15,'bold'))
    CpfLabel.grid(row=0,column=0, padx=5, pady=5)
    CpfEntry = Entry(JanelaAtualizarCliente, width=30)
    CpfEntry.grid(row=0,column=1, padx=5, pady=5)
    
    NomeLabel = Label(JanelaAtualizarCliente, text='Nome:', font=('trebuchet ms',15,'bold'))
    NomeLabel.grid(row=1,column=0, padx=5, pady=5)
    NomeEntry = Entry(JanelaAtualizarCliente, width=30)
    NomeEntry.grid(row=1,column=1, padx=5, pady=5)
    
    EndereçoLabel = Label(JanelaAtualizarCliente, text='Endereço:', font=('trebuchet ms',15,'bold'))
    EndereçoLabel.grid(row=2,column=0, padx=5, pady=5)
    EndereçoEntry = Entry(JanelaAtualizarCliente, width=30)
    EndereçoEntry.grid(row=2,column=1, padx=5, pady=5)
    
    TelefoneLabel = Label(JanelaAtualizarCliente, text='Telefone:', font=('trebuchet ms',15,'bold'))
    TelefoneLabel.grid(row=3,column=0, padx=5, pady=5)
    TelefoneEntry = Entry(JanelaAtualizarCliente, width=30)
    TelefoneEntry.grid(row=3,column=1, padx=5, pady=5)
    
    EmailLabel = Label(JanelaAtualizarCliente, text='Email:', font=('trebuchet ms',15,'bold'))
    EmailLabel.grid(row=4,column=0, padx=5, pady=5)
    EmailEntry = Entry(JanelaAtualizarCliente, width=30)
    EmailEntry.grid(row=4,column=1, padx=5, pady=5)
    
    CompraLabel = Label(JanelaAtualizarCliente, text='Compra:', font=('trebuchet ms',15,'bold'))
    CompraLabel.grid(row=5,column=0, padx=5, pady=5)
    CompraEntry = Entry(JanelaAtualizarCliente, width=30)
    CompraEntry.grid(row=5,column=1, padx=5, pady=5)
    
    FPLabel = Label(JanelaAtualizarCliente, text='F. Pagamento:', font=('trebuchet ms',15,'bold'))
    FPLabel.grid(row=6,column=0, padx=5, pady=5)
    FPEntry = Entry(JanelaAtualizarCliente, width=30)
    FPEntry.grid(row=6,column=1, padx=5, pady=5)
    
    AtualizarBotao = Button(JanelaAtualizarCliente, text='Atualizar',activebackground='white', cursor='hand2',command=AtualizarDadosCliente)
    AtualizarBotao.grid(row=7,column=1,pady=5)
    
    indexing = Topicos.focus()
    print(indexing)
    conteudo = Topicos.item(indexing)
    listaDados = conteudo['values']
    CpfEntry.insert(0,listaDados[0])
    NomeEntry.insert(0,listaDados[1])
    EndereçoEntry.insert(0,listaDados[2])
    TelefoneEntry.insert(0,listaDados[3])
    EmailEntry.insert(0,listaDados[4])
    CompraEntry.insert(0,listaDados[5])
    FPEntry.insert(0,listaDados[6])

def ListarCliente():
    Query = 'select * from alldata'
    meuCursor.execute(Query)
    CataDados = meuCursor.fetchall()
    Topicos.delete(*Topicos.get_children())
    for data in CataDados:
        Topicos.insert('',END,values=data)
    
def DeletarCliente(): #Deleta pelo CPF
    indexing = Topicos.focus()
    print(indexing)
    
    conteudo = Topicos.item(indexing)
    conteudoCPF = conteudo['values'][0]
    Query = 'delete from alldata where cpf=%s'
    meuCursor.execute(Query,conteudoCPF)
    con.commit()
    messagebox.showinfo('Deletado','Cliente deletado com sucesso.')
    
    Query = 'select * from alldata'
    meuCursor.execute(Query)
    CataDados = meuCursor.fetchall()
    Topicos.delete(*Topicos.get_children())
    for data in CataDados:
        Topicos.insert('',END,values=data)
        
def ProcurarCliente():
    def ProcurarDadosCliente():
        Query = 'select * from alldata where cpf=%s or nome=%s or endereço=%s or telefone=%s or email=%s or compra=%s or formapagamento=%s'
        meuCursor.execute(Query,(CpfEntry.get(),NomeEntry.get(),EndereçoEntry.get(),TelefoneEntry.get(), EmailEntry.get(),CompraEntry.get(),FPEntry.get()))
        Topicos.delete(*Topicos.get_children())
        CataDados = meuCursor.fetchall()
        for data in CataDados:
            Topicos.insert('',END,values=data)
            
    JanelaProcurarCliente = Toplevel()
    JanelaProcurarCliente.title('Procurar Cliente')
    JanelaProcurarCliente.resizable(False,False)
    JanelaProcurarCliente.grab_set()
    
    CpfLabel = Label(JanelaProcurarCliente, text='Cpf:', font=('trebuchet ms',15,'bold'))
    CpfLabel.grid(row=0,column=0, padx=5, pady=5)
    CpfEntry = Entry(JanelaProcurarCliente, width=30)
    CpfEntry.grid(row=0,column=1, padx=5, pady=5)
    
    NomeLabel = Label(JanelaProcurarCliente, text='Nome:', font=('trebuchet ms',15,'bold'))
    NomeLabel.grid(row=1,column=0, padx=5, pady=5)
    NomeEntry = Entry(JanelaProcurarCliente, width=30)
    NomeEntry.grid(row=1,column=1, padx=5, pady=5)
    
    EndereçoLabel = Label(JanelaProcurarCliente, text='Endereço:', font=('trebuchet ms',15,'bold'))
    EndereçoLabel.grid(row=2,column=0, padx=5, pady=5)
    EndereçoEntry = Entry(JanelaProcurarCliente, width=30)
    EndereçoEntry.grid(row=2,column=1, padx=5, pady=5)
    
    TelefoneLabel = Label(JanelaProcurarCliente, text='Telefone:', font=('trebuchet ms',15,'bold'))
    TelefoneLabel.grid(row=3,column=0, padx=5, pady=5)
    TelefoneEntry = Entry(JanelaProcurarCliente, width=30)
    TelefoneEntry.grid(row=3,column=1, padx=5, pady=5)
    
    EmailLabel = Label(JanelaProcurarCliente, text='Email:', font=('trebuchet ms',15,'bold'))
    EmailLabel.grid(row=4,column=0, padx=5, pady=5)
    EmailEntry = Entry(JanelaProcurarCliente, width=30)
    EmailEntry.grid(row=4,column=1, padx=5, pady=5)
    
    CompraLabel = Label(JanelaProcurarCliente, text='Compra:', font=('trebuchet ms',15,'bold'))
    CompraLabel.grid(row=5,column=0, padx=5, pady=5)
    CompraEntry = Entry(JanelaProcurarCliente, width=30)
    CompraEntry.grid(row=5,column=1, padx=5, pady=5)
    
    FPLabel = Label(JanelaProcurarCliente, text='F. Pagamento:', font=('trebuchet ms',15,'bold'))
    FPLabel.grid(row=6,column=0, padx=5, pady=5)
    FPEntry = Entry(JanelaProcurarCliente, width=30)
    FPEntry.grid(row=6,column=1, padx=5, pady=5)
    
    ProcurarBotao = Button(JanelaProcurarCliente, text='Procurar',activebackground='white', cursor='hand2', command=ProcurarDadosCliente)
    ProcurarBotao.grid(row=7,column=1,pady=5)

def AddCliente():
    def AddDadosCliente():
        if CpfEntry.get()=='' or NomeEntry.get()=='' or EndereçoEntry.get()=='' or TelefoneEntry.get()=='' or EmailEntry.get()=='' or CompraEntry.get()=='' or FPEntry.get()=='':
            messagebox.showerror('Erro','Todos os campos devem ser preenchidos.', parent=JanelaAddCliente)
        else:
            data = date.today()
            horario = time.strftime('%H:%M:%S')
            Query = 'insert into alldata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            meuCursor.execute(Query,(CpfEntry.get(), NomeEntry.get(),EndereçoEntry.get(),TelefoneEntry.get(),
                                    EmailEntry.get(), CompraEntry.get(),data,horario,FPEntry.get()))
            con.commit()
            resultado = messagebox.askyesno('Sucesso','Cliente adicionado. Gostaria de limpar o questionário?',parent=JanelaAddCliente)
            if resultado:
                CpfEntry.delete(0,END)
                NomeEntry.delete(0,END)
                EndereçoEntry.delete(0,END)
                TelefoneEntry.delete(0,END)
                EmailEntry.delete(0,END)
                CompraEntry.delete(0,END)
                FPEntry.delete(0,END)
            else:
                pass
    
            Query = 'select *from alldata'
            meuCursor.execute(Query)
            CataDados = meuCursor.fetchall()
            Topicos.delete(*Topicos.get_children())
            for data in CataDados:
                Topicos.insert('',END,values=data)
    
    JanelaAddCliente = Toplevel()
    JanelaAddCliente.title('Adicionar Cliente')
    JanelaAddCliente.resizable(False,False)
    JanelaAddCliente.grab_set()
    
    CpfLabel = Label(JanelaAddCliente, text='Cpf:', font=('trebuchet ms',15,'bold'))
    CpfLabel.grid(row=0,column=0, padx=5, pady=5)
    CpfEntry = Entry(JanelaAddCliente, width=30)
    CpfEntry.grid(row=0,column=1, padx=5, pady=5)
    
    NomeLabel = Label(JanelaAddCliente, text='Nome:', font=('trebuchet ms',15,'bold'))
    NomeLabel.grid(row=1,column=0, padx=5, pady=5)
    NomeEntry = Entry(JanelaAddCliente, width=30)
    NomeEntry.grid(row=1,column=1, padx=5, pady=5)
    
    EndereçoLabel = Label(JanelaAddCliente, text='Endereço:', font=('trebuchet ms',15,'bold'))
    EndereçoLabel.grid(row=2,column=0, padx=5, pady=5)
    EndereçoEntry = Entry(JanelaAddCliente, width=30)
    EndereçoEntry.grid(row=2,column=1, padx=5, pady=5)
    
    TelefoneLabel = Label(JanelaAddCliente, text='Telefone:', font=('trebuchet ms',15,'bold'))
    TelefoneLabel.grid(row=3,column=0, padx=5, pady=5)
    TelefoneEntry = Entry(JanelaAddCliente, width=30)
    TelefoneEntry.grid(row=3,column=1, padx=5, pady=5)
    
    EmailLabel = Label(JanelaAddCliente, text='Email:', font=('trebuchet ms',15,'bold'))
    EmailLabel.grid(row=4,column=0, padx=5, pady=5)
    EmailEntry = Entry(JanelaAddCliente, width=30)
    EmailEntry.grid(row=4,column=1, padx=5, pady=5)
    
    CompraLabel = Label(JanelaAddCliente, text='Compra:', font=('trebuchet ms',15,'bold'))
    CompraLabel.grid(row=5,column=0, padx=5, pady=5)
    CompraEntry = Entry(JanelaAddCliente, width=30)
    CompraEntry.grid(row=5,column=1, padx=5, pady=5)
    
    FPLabel = Label(JanelaAddCliente, text='F. Pagamento:', font=('trebuchet ms',15,'bold'))
    FPLabel.grid(row=6,column=0, padx=5, pady=5)
    FPEntry = Entry(JanelaAddCliente, width=30)
    FPEntry.grid(row=6,column=1, padx=5, pady=5)
    
    AdicionarBotao = Button(JanelaAddCliente, text='Adicionar',activebackground='white', cursor='hand2', command=AddDadosCliente)
    AdicionarBotao.grid(row=7,column=1,pady=5)
    
def Relogio():
    global data, horario
    data = date.today()
    horario = time.strftime('%H:%M:%S')
    LabelDataHorario.config(text=f'  Data: {data} \n  Horário: {horario}')
    LabelDataHorario.after(1000, Relogio)    


#host=localhost
#username=root
#password=32462584
#database=bdcliente
def ConectarBD():
    def ComandoConectar():
        global con, meuCursor
        try:
            con = pymysql.connect(host='localhost',user='root',password='32462584')
            meuCursor = con.cursor()
        except:
            messagebox.showerror('Erro!', 'Os dados inseridos são inválidos.', parent=Janelinha)
            return
        try:
            Query = 'create database BDCliente'
            meuCursor.execute(Query)
            Query = 'use BDCliente'
            meuCursor.execute(Query)
            Query = 'create table alldata(cpf varchar(30),nome varchar(30),endereço varchar(30),telefone varchar(30), email varchar(30), compra varchar(30), formapagamento varchar(30), data varchar(30), horario varchar(30))'
            meuCursor.execute(Query)
        except:
            Query = 'use BDCliente'
            meuCursor.execute(Query)
        messagebox.showinfo('Sucesso!', 'Conexão com o banco de dados realizada!', parent=Janelinha)
        Janelinha.destroy()
        BotaoAddCliente.config(state=NORMAL)
        BotaoAtualizarCliente.config(state=NORMAL)
        BotaoPesquisarCliente.config(state=NORMAL)
        BotaoDeletarCliente.config(state=NORMAL)
        BotaoListarCliente.config(state=NORMAL)
        BotaoExportarDadosCliente.config(state=NORMAL)
        
    Janelinha = Toplevel()
    Janelinha.grab_set()
    Janelinha.geometry('250x200+730+230')
    Janelinha.title('Conectar BD')
    Janelinha.resizable(False, False)
    
    LabelServidor = Label(Janelinha, text='Servidor:', font=('trebuchet ms',10,'bold'))
    LabelServidor.grid(row=0,column=0, padx=10)
    EntryServidor = Entry(Janelinha, bd=2)
    EntryServidor.grid(row=0,column=1, padx=2, pady=5)
                                                            
    LabelUsuario = Label(Janelinha, text='Usuário:', font=('trebuchet ms',10,'bold'))
    LabelUsuario.grid(row=1,column=0, padx=10)
    EntryUsuario = Entry(Janelinha, bd=2)
    EntryUsuario.grid(row=1,column=1, padx=2, pady=5)
    
    LabelSenha = Label(Janelinha, text='Senha:', font=('trebuchet ms',10,'bold'))
    LabelSenha.grid(row=2,column=0, padx=10)
    EntrySenha = Entry(Janelinha, bd=2)
    EntrySenha.grid(row=2,column=1, padx=2, pady=5)
    
    BotaoConectarBD = Button(Janelinha, text='Conectar', activebackground='white', cursor='hand2',command=ComandoConectar)
    BotaoConectarBD.grid(row=3,column=1)                                        

Janela2 = Tk()

Janela2.geometry('1174x680+0+0')
Janela2.resizable(False, False)
Janela2.title('Guerenciamento Lojinha')

LabelDataHorario = Label(Janela2, text='opa', font=('trebuchet ms',10))
LabelDataHorario.place(x=5,y=5)
Relogio()

x = 'CRUD Lojinha - Clientes'
Titulo = Label(Janela2, text= x, font = ('trebuchet ms',28,'bold'), width=30)
Titulo.place(x=200,y=0)

BotaoConnect = Button(Janela2, text='Conectar Banco de Dados', activebackground='white', cursor='hand2',command=ConectarBD)
BotaoConnect.place(x=980,y=15)

BotaoProxPg1 = Button(Janela2, text='Funcionários >>>', activebackground='white', cursor='hand2')
BotaoProxPg1.place(x=980,y=45)

    # Conteúdo Frame Esquerdo
FrameEsquerda = Frame(Janela2)
FrameEsquerda.place(x=50,y=80,width=300,height=600)

ImagemLogo = PhotoImage(file='Jaqueta.png')
LabelLogo = Label(FrameEsquerda, image=ImagemLogo)
LabelLogo.grid(row=0,column=0)

ImagemLogo2 = PhotoImage(file='Luva.png')
LabelLogo2 = Label(FrameEsquerda, image=ImagemLogo2)
LabelLogo2.grid(row=0,column=1)

ImagemLogo3 = PhotoImage(file='Gorro.png')
LabelLogo3 = Label(FrameEsquerda, image=ImagemLogo3)
LabelLogo3.grid(row=0,column=2)

ImagemLogo4 = PhotoImage(file='Girl.png')
LabelLogo4 = Label(Janela2, image=ImagemLogo4)
LabelLogo4.place(x=730,y=0)

BotaoAddCliente = Button(FrameEsquerda, text='Adicionar Cliente', activebackground='white', cursor='hand2',width=20,command=AddCliente)
BotaoAddCliente.grid(row=1,column=1,pady=20)

BotaoPesquisarCliente = Button(FrameEsquerda, text='Pesquisar Cliente', activebackground='white', cursor='hand2',width=20,command=ProcurarCliente)
BotaoPesquisarCliente.grid(row=2,column=1,pady=20)

BotaoDeletarCliente = Button(FrameEsquerda, text='Deletar Cliente', activebackground='white', cursor='hand2',width=20, command=DeletarCliente)
BotaoDeletarCliente.grid(row=3,column=1,pady=20)

BotaoAtualizarCliente = Button(FrameEsquerda, text='Atualizar Cliente', activebackground='white', cursor='hand2',width=20, command=AtualizarCliente)
BotaoAtualizarCliente.grid(row=4,column=1,pady=20)

BotaoListarCliente = Button(FrameEsquerda, text='Listar Cliente', activebackground='white', cursor='hand2',width=20,command=ListarCliente)
BotaoListarCliente.grid(row=5,column=1,pady=20)

BotaoExportarDadosCliente = Button(FrameEsquerda, text='Exportar Dados', activebackground='white', cursor='hand2',width=20)
BotaoExportarDadosCliente.grid(row=6,column=1,pady=20)

BotaoSairCliente = Button(FrameEsquerda, text='Sair', activebackground='orange2', cursor='hand2',width=20)
BotaoSairCliente.grid(row=7,column=1,pady=20)

    # Conteúdo Frame Direito
FrameDireita= Frame(Janela2)
FrameDireita.place(x=350,y=80,width=780,height=550)

ScrollBarX = Scrollbar(FrameDireita,orient=HORIZONTAL)


Topicos = ttk.Treeview(FrameDireita, columns=('Cpf','Nome','Endereço','Telefone','Email','Compra','Data','Horario','Forma de Pagamento'),
                       xscrollcommand=ScrollBarX.set)
Topicos.pack(fill=BOTH,expand=1)

ScrollBarX.config(command=Topicos.xview)
ScrollBarX.pack(side=BOTTOM, fill=X)

Topicos.heading('Cpf',text='Cpf')
Topicos.heading('Nome',text='Nome')
Topicos.heading('Endereço',text='Endereço')
Topicos.heading('Telefone',text='Telefone')
Topicos.heading('Email',text='Email')
Topicos.heading('Compra',text='Compra')
Topicos.heading('Data',text='Data')
Topicos.heading('Horario',text='Horario')
Topicos.heading('Forma de Pagamento',text='Forma de Pagamento')
Topicos.config(show='headings')

Janela2.mainloop()
