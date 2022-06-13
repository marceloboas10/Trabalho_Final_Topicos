from tkinter import*
from imports import *
from relatorios import *
from funcoes import Funcoes

#váriável para criar a janela Tkinter
telaTk = Tk()
loginaprovado = 0

class Login(Funcoes):
    def __init__(self): # Inicialização da classe
        self.telaTk = telaTk
        self.tela()
        self.frames_tela()
        self.cria_botao()
        telaTk.mainloop() # Criar um loop para abrir a janela

    def tela(self):
        self.telaTk.title('Login') # Title cria o titulo do Tkinter
        self.telaTk.geometry('400x400') # Tamanho da tela
        self.telaTk.maxsize(width=800, height=600) #Tamanho maximo da tela
        self.telaTk.minsize(width=200, height=200) #Tamanho minimo da tela
        self.telaTk.resizable(True, True) # Tela responsiva
        self.telaTk.configure(background='#1e3743') # Cor de fundo
    
    def frames_tela(self):
        self.frame = Frame(self.telaTk, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        
    def cria_botao(self):
        # Label Login
        self.label_codigo = Label(self.frame, text='Login (E-mail)', bg = '#dfe3ee',fg='#000000', font=('Calibri', '14', 'bold'))
        self.label_codigo.place(relx=0.03, rely=0.21)

        # Entry Login
        self.fontePadrao=("Calibri","14")
        self.entry_login = Entry(self.telaTk)
        self.entry_login["font"]=self.fontePadrao
        self.entry_login.place(relx=0.066, rely=0.3, relwidth=0.87, relheight=0.08)

        # Label Senha
        self.label_codigo = Label(self.frame, text='Senha', bg = '#dfe3ee',fg='#000000', font=('Calibri', '14', 'bold'))
        self.label_codigo.place(relx=0.03, rely=0.39)

        # Entry senha 
        self.entry_senha = Entry(self.telaTk, show="*")
        self.entry_senha["font"]=self.fontePadrao
        self.entry_senha.place(relx=0.066, rely=0.46, relwidth=0.87, relheight=0.08)
        self.entry_senha["show"]= '*'

        # Botão Entrar
        self.botaoCadclientes = Button(self.frame,text='Entrar',border=2 ,bg='#109db2', fg='white', font = ('Calibri', 14, 'bold'), command= self.validar_usuario)
        self.botaoCadclientes.place(relx=0.35, rely=0.65, relwidth=0.3, relheight=0.14)

        # LABELS

        self.label_codigo = Label(self.frame, text='L&M Sistemas', bg = '#dfe3ee',fg='#000000', font=('Calibri', 24, 'bold'))
        self.label_codigo.place(relx=0.24, rely=0.02)

    #Método para fechar tela
    def fechaTela(self):
        self.telaTk.destroy()

    #Metodo para Cadastrar Usuario
    def telaCadastro(self):
        self.telaTk.destroy()
        from cad_usuarios import Usuarios
    
    def validar_usuario(self):
        
        login = self.entry_login.get()
        senha = self.entry_senha.get()

        if (login == ""):
            messagebox.showinfo('Erro Sistema', 'Digite o E-mail e a Senha')
        else:
            self.conectar_sql()
            self.cursor.execute(
                """ SELECT nomeuser, email, senha FROM usuarios
                ORDER BY nomeuser ASC""")
            data = self.cursor.fetchall()
            num = len(data)
            
            if(num == 0):
                self.insert_Padrao()
                messagebox.showinfo('Primeiro Acesso', 'Use o usuário: admin@admin e a senha: masteradmin para primeiro acesso')
            else:
                self.conectar_sql()
                self.cursor.execute(
                    """ SELECT email, senha FROM usuarios
                    WHERE email LIKE '%s' ORDER BY nomeuser ASC""" %login)
                buscanomeCliente = self.cursor.fetchall()
                Passw = buscanomeCliente[0]         
                Login = (login, senha)

                self.desconecta_sql
                        
                if(Login == Passw):
                    self.telaTk.destroy()
                    from menu import Menu
                else:
                    messagebox.showinfo('Erro Sistema', 'E-mail ou Senha inválidos!')       
Login()



