from imports import *
from funcoes import Funcoes
import tkinter as tk

class Usuarios(Funcoes):
    def usuarios(self): # Inicialização da classe
        self.teladeUsuarios = tk.Toplevel()
        self.telaUsuarios()
        self.frames_telaUsuarios()
        self.cria_botaoUsuarios()
        self.criar_tabela_cadUsuarios()
        self.select_cadUsuario()
        #self.menus()

    def telaUsuarios(self):
        self.teladeUsuarios.title('Cadastro de Usuários') # Title cria o titulo do Tkinter
        self.teladeUsuarios.geometry('980x600') # Tamanho da tela
        self.teladeUsuarios.maxsize(width=980, height=600) #Tamanho maximo da tela
        self.teladeUsuarios.minsize(width=600, height=460) #Tamanho minimo da tela
        self.teladeUsuarios.resizable(True, True) # Tela responsiva
        self.teladeUsuarios.configure(background='#1e3743') # Cor de fundo

    def frames_telaUsuarios(self):
        self.frame = Frame(self.teladeUsuarios, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def cria_botaoUsuarios(self):
        # Botão Buscar
        self.botaoBuscar = Button(self.frame, text='Buscar', border=2, bg='#109db2', fg='white', font = ('verdana', 8 , 'bold'), command=self.buscar_usuario)
        self.botaoBuscar.place(relx=0.02, rely=0.9, relwidth=0.1, relheight=0.05)

        # Botão Cadastrar
        self.botaoNovo = Button(self.frame, text='Cadastrar', border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command=self.insert_cadUsuario)
        self.botaoNovo.place(relx=0.15, rely=0.9, relwidth=0.1,relheight=0.05)

        # Botão Alterar
        self.botaoAlterar = Button(self.frame, text='Alterar',border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command= self.alterar_usuario)
        self.botaoAlterar.place(relx=0.28, rely=0.9, relwidth=0.1, relheight=0.05)

        # Botão Voltar
        self.botaoApagar = Button(self.frame, text='Voltar para Menu',border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command= self.voltarMenuUsuarios)
        self.botaoApagar.place(relx=0.54, rely=0.9, relwidth=0.15, relheight=0.05)

        # Botão Apagar
        self.botaoApagar = Button(self.frame, text='Apagar',border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command= self.deleta_usuarios)
        self.botaoApagar.place(relx=0.41, rely=0.9, relwidth=0.1, relheight=0.05)

        # LABELS

        self.label_codigo = Label(self.frame, text='CADASTRO DE USUÁRIOS', bg = '#dfe3ee',fg='#000000', font=('Calibri', 22, 'bold'))
        self.label_codigo.place(relx=0.02, rely=0.02)

        # Criação do label Nome de Usuário
        self.label_nomeuser = Label(self.frame, text="Nome:", bg = '#dfe3ee',fg='#109db2', font=('calibri', 14, 'bold'))
        self.label_nomeuser.place(relx=0.02, rely=0.1)
        self.entry_nomeuser = Entry(self.frame, font=('calibri', 14, 'bold'))
        self.entry_nomeuser.place(relx=0.02, rely=0.15, relwidth=0.7, relheight=0.05)

        # Criação do label E-mail
        self.label_email = Label(self.frame, text="E-mail:", bg = '#dfe3ee',fg='#109db2', font=('calibri', 14, 'bold'))
        self.label_email.place(relx=0.02, rely=0.2)
        self.entry_email = Entry(self.frame, font=('calibri', 14, 'bold'))
        self.entry_email.place(relx=0.02, rely=0.25, relwidth=0.5,  relheight=0.05)

        # Criação do label senha1
        self.label_senha1 = Label(self.frame, text="Senha:", bg = '#dfe3ee',fg='#109db2', font=('calibri', 14, 'bold'))
        self.label_senha1.place(relx= 0.02, rely=0.3)
        self.entry_senha1 = Entry(self.frame, font=('calibri', 14, 'bold'))
        self.entry_senha1.place(relx=0.02, rely=0.35, relwidth=0.3, relheight=0.05)
        self.entry_senha1["show"]= '*'

        # Criação do label senha2
        self.label_senha2 = Label(self.frame, text="Confirmação da Senha:", bg = '#dfe3ee',fg='#109db2', font=('calibri', 14, 'bold'))
        self.label_senha2.place(relx= 0.02, rely=0.4)
        self.entry_senha2 = Entry(self.frame, font=('calibri', 14, 'bold'))
        self.entry_senha2.place(relx=0.02, rely=0.45, relwidth=0.3, relheight=0.05)
        self.entry_senha2["show"]= '*'

        # Criação do Combobox tipo de usuário

        self.lista_menu_users = ttk.Treeview(self.frame, height=3, column=('col1','col2'))
        self.lista_menu_users.heading('#1',text='Nome')
        self.lista_menu_users.heading('#2',text='E-mail')

        # Tamanho das colunas em relação ao quadro (quadro tem 500)
        self.lista_menu_users.column('#0',width=1)
        self.lista_menu_users.column('#1',width=99)
        self.lista_menu_users.column('#1',width=200)

        # Criação da lista
        self.lista_menu_users.place(relx=0.02,rely=0.55, relwidth=0.9, relheight=0.3)

        # Barra de rolagem lateral
        self.scrollLista = Scrollbar(self.frame, orient='vertical')
        self.lista_menu_users.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.91, rely=0.55, relwidth=0.04, relheight=0.3)
        self.lista_menu_users.bind('<Double-1>', self.duplo_clickUsuarios)
    
    def voltarMenuUsuarios(self):
        self.teladeUsuarios.destroy()

Usuarios()