from imports import *
from funcoes import Funcoes
import tkinter as tk


class Sobre(Funcoes):
    def sobre(self): # Inicialização da classe
        self.telaSobre = tk.Toplevel()
        self.tela()   
        self.cria_tela()             
        #telaSobre.mainloop() # Criar um loop para abrir a janela

    def tela(self):
        self.telaSobre.title("Sobre")
        self.telaSobre.geometry("980x600+610+153")
        #master.iconbitmap(default="icones\\ico.ico")
        self.telaSobre.resizable(width=1, height=1)

    def cria_tela(self):
        #importar imagens
        self.img_fundo = PhotoImage(file="P2_topicos\\imagens\\Sobre.png")

        #Criação de Labels
        
        self.fundo = Label(self.telaSobre, image=self.img_fundo)
        self.fundo.pack()
       
        # Botão Voltar
        self.botaoApagar = Button(self.telaSobre, text='Voltar para Menu',border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command= self.voltarMenuSobre)
        self.botaoApagar.place(relx=0.8, rely=0.9, relwidth=0.15, relheight=0.05)
       
    
    # # Criação Menu
    # def menus(self):
    #     menu_bar = Menu(self.telaSobre)
    #     self.telaSobre.config(menu=menu_bar)
    #     file_menu = Menu(menu_bar, tearoff=0)
    #     file_menu2 = Menu(menu_bar, tearoff=0)

    #     def quit(): self.telaSobre.destroy()

    #     menu_bar.add_cascade(label= 'Opções', menu = file_menu)
    #     menu_bar.add_cascade(label= 'Relatórios', menu = file_menu2)
        
    #     file_menu.add_command(label='Sair', command= quit)
    #     file_menu2.add_command(label='Ficha do cliente', command= self.geraRelatorio)

    def voltarMenuSobre(self):
        self.telaSobre.destroy()

Sobre()