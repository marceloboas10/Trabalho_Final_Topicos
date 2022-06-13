from imports import *
from exportar_dados import Exportar
from cad_clientes import Clientes
from cad_fornecedores import Fornecedores
from cad_usuarios import Usuarios
from cad_produtos import Produtos
from sobre import Sobre
from cota_moeda import Moeda
import tkinter as tk

# telaMenu = Tk() # Variável para criar a janela Tkinter

class Menu(Clientes, Fornecedores, Usuarios, Produtos, Sobre, Moeda, Exportar):
    def __init__(self): # Inicialização da classe
        self.telaMenu = tk.Tk()
        self.tela()
        self.frames_tela()
        self.cria_botao()
        self.telaMenu.mainloop() # Criar um loop para abrir a janela

    def tela(self):
        self.telaMenu.title('Menu') # Title cria o titulo do Tkinter
        self.telaMenu.geometry('980x600') # Tamanho da tela
        self.telaMenu.maxsize(width=980, height=600) #Tamanho maximo da tela
        self.telaMenu.minsize(width=600, height=460) #Tamanho minimo da tela
        self.telaMenu.resizable(True, True) # Tela responsiva
        self.telaMenu.configure(background='#1e3743') # Cor de fundo       

    def frames_tela(self):
        self.frame = Frame(self.telaMenu, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        
        
    def cria_botao(self):
        # Botão Cadastro de Clientes
        self.botaoCadclientes = Button(self.frame,text='Cadastro de Clientes',border=2 ,bg='#109db2', fg='white', font = ('Calibri', 18, 'bold'), command= self.clientes)
        self.botaoCadclientes.place(relx=0.02, rely=0.1, relwidth=0.6, relheight=0.09)
        self.labelCadclientes = Label(self.frame, text='Cadastro dos dados dos Clientes (nome,\nendereço, cidade, estado, telefone) no sistema', bg = '#dfe3ee',fg='#000000', font=('Calibri', 12, 'bold'))
        self.labelCadclientes.place(relx=0.64, rely=0.1)

        # Botão Cadastro de Usuarios
        self.botaoCadusuarios = Button(self.frame, text='Cadastro de Usuários', border=2, bg='#109db2', fg='white', font = ('Calibri', 18 , 'bold'), command=self.usuarios)
        self.botaoCadusuarios.place(relx=0.02, rely=0.21, relwidth=0.6, relheight=0.09)
        self.labelCadusuarios = Label(self.frame, text='Cadastro do nome, login e senha dos usuários\n do sistema', bg = '#dfe3ee',fg='#000000', font=('Calibri', 12, 'bold'))
        self.labelCadusuarios.place(relx=0.64, rely=0.21)


        # # Botão Cadastro de Produtos
        self.botaoCadprodutos = Button(self.frame, text='Cadastro de Produtos', border=2, bg='#109db2', fg='white', font = ('Calibri', 18 , 'bold'), command=self.produtos)
        self.botaoCadprodutos.place(relx=0.02, rely=0.32, relwidth=0.6, relheight=0.09)
        self.labelCadprodutos = Label(self.frame, text='Cadastro dos dados dos produtos no sistema', bg = '#dfe3ee',fg='#000000', font=('Calibri', 12, 'bold'))
        self.labelCadprodutos.place(relx=0.64, rely=0.32)

        # # Botão Cadastro de Fornecedores
        self.botaoCadFornecedores = Button(self.frame, text='Cadastro de Fornecedores', border=2, bg='#109db2', fg='white', font = ('Calibri', 18 , 'bold'), command=self.fornecedores)
        self.botaoCadFornecedores.place(relx=0.02, rely=0.43, relwidth=0.6, relheight=0.09)
        self.labelCadFornecedores = Label(self.frame, text='Cadastro dos dados dos fornecedores (nome,\n endereço, cidade, estado, telefone) no sistema', bg = '#dfe3ee',fg='#000000', font=('Calibri', 12, 'bold'))
        self.labelCadFornecedores.place(relx=0.64, rely=0.43)

        # # Botão Cotações Moedas Estrangeiras
        self.botaoGeraPedido = Button(self.frame, text='Cotação de Dolar, Euro e Bitcoin', border=2, bg='#109db2', fg='white', font = ('Calibri', 18 , 'bold'), command=self.moeda)
        self.botaoGeraPedido.place(relx=0.02, rely=0.54, relwidth=0.6, relheight=0.09)
        self.labelCadFornecedores = Label(self.frame, text='Faz a cotação automática dos valores\n na internet e converte o valor desejado', bg = '#dfe3ee',fg='#000000', font=('Calibri', 12, 'bold'))
        self.labelCadFornecedores.place(relx=0.64, rely=0.54)

        # # Botão Exportar
        self.botaoExportar = Button(self.frame, text='Exportar Dados', border=2, bg='#109db2', fg='white', font = ('Calibri', 18 , 'bold'), command=self.exportar)
        self.botaoExportar.place(relx=0.02, rely=0.65, relwidth=0.6, relheight=0.09)
        self.labelExportar = Label(self.frame, text='Exporta todos os dados do Banco de dados\n para um arquivo JSON compactado em zip', bg = '#dfe3ee',fg='#000000', font=('Calibri', 12, 'bold'))
        self.labelExportar.place(relx=0.64, rely=0.65)

        # # Botão Sobre
        self.botaoSobre = Button(self.frame, text='Sobre o M&L Sistemas', border=2, bg='#109db2', fg='white', font = ('Calibri', 18 , 'bold'), command=self.sobre)
        self.botaoSobre.place(relx=0.02, rely=0.76, relwidth=0.6, relheight=0.09)
        self.labelSobre = Label(self.frame, text='Informações sobre o sistema e sobre\n os desenvolvedores do sistema', bg = '#dfe3ee',fg='#000000', font=('Calibri', 12, 'bold'))
        self.labelSobre.place(relx=0.64, rely=0.76)

        # # Botão Sair
        self.botaoSair = Button(self.frame, text='Sair', border=2, bg='#109db2', fg='red', font = ('Calibri', 18 , 'bold'), command=self.fechaTela)
        self.botaoSair.place(relx=0.02, rely=0.87, relwidth=0.6, relheight=0.09)

        # LABELS

        self.label_codigo = Label(self.frame, text='MENU PRINCIPAL', bg = '#dfe3ee',fg='#000000', font=('Calibri', 22, 'bold'))
        self.label_codigo.place(relx=0.02, rely=0.02, relwidth=0.6)
    
    def fechaTela(self):
        self.telaMenu.destroy()
    
    

    # def switch_frame(self, frame_class):
    #     new_frame = frame_class(self)
    #     if self._frame is not None:
    #         self._frame.destroy()
    #     self._frame = new_frame
    #     self._frame.pack()


Menu()