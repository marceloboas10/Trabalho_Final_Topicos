from imports import *
from relatorios import *
from funcoes import Funcoes

import tkinter as tk

class Exportar(Funcoes):
    def exportar(self): # Inicialização da classe
        self.telaExportar = tk.Toplevel()
        self.tela_exportar()
        self.frames_telaExportar()
        self.cria_botaoExportar()
        #self.select_cadCliente()
        # self.lista_clientes()
        # self.listaprodutos()
        # self.listaPedidos()
        # self.criar_tabela_cadCliente()
        # self.select_cadCliente_Pedido()

    def tela_exportar(self):
        self.telaExportar.title('Gerar Pedidos') # Title cria o titulo do Tkinter
        self.telaExportar.geometry('980x600') # Tamanho da tela
        self.telaExportar.maxsize(width=980, height=600) #Tamanho maximo da tela
        self.telaExportar.minsize(width=600, height=460) #Tamanho minimo da tela
        self.telaExportar.configure(background='#1e3743') # Cor de fundo

    def frames_telaExportar(self):
        self.frame_1 = Frame(self.telaExportar, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.225)
        self.frame_2 = Frame(self.telaExportar, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.265, relwidth=0.96, relheight=0.225)
        self.frame_3 = Frame(self.telaExportar, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_3.place(relx=0.02, rely=0.51, relwidth=0.96, relheight=0.225)
        self.frame_4 = Frame(self.telaExportar, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_4.place(relx=0.02, rely=0.755, relwidth=0.96, relheight=0.225)

    def cria_botaoExportar(self):
        # Botão Exportar Clientes
        self.btnExportarClientes = Button(self.frame_1,text='Exportar Clientes',border=2 ,bg='#109db2', fg='white', font = ('verdana', 12, 'bold'), command= self.exportar_Clientes)
        self.btnExportarClientes.place(relx=0.02, rely=0.5, relwidth=0.3, relheight=0.4)

        # Botão Exportar Fornecedores
        self.btnExportarClientes = Button(self.frame_2,text='Exportar Fornecedores',border=2 ,bg='#109db2', fg='white', font = ('verdana', 12, 'bold'), command= self.exportar_Fornecedores)
        self.btnExportarClientes.place(relx=0.02, rely=0.5, relwidth=0.3, relheight=0.4)

        # Botão Exportar Produtos
        self.btnExportarClientes = Button(self.frame_3,text='Exportar Produtos',border=2 ,bg='#109db2', fg='white', font = ('verdana', 12, 'bold'), command= self.exportar_Produtos)
        self.btnExportarClientes.place(relx=0.02, rely=0.5, relwidth=0.3, relheight=0.4)

        # Botão Exportar Usuários
        self.btnExportarClientes = Button(self.frame_4,text='Exportar Usuários',border=2 ,bg='#109db2', fg='white', font = ('verdana', 12, 'bold'), command= self.exportar_Usuarios)
        self.btnExportarClientes.place(relx=0.02, rely=0.5, relwidth=0.3, relheight=0.4)

        # Botão Voltar
        self.botaoVoltar = Button(self.frame_4, text='Voltar para Menu',border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command= self.voltarMenuExportar)
        self.botaoVoltar.place(relx=0.85, rely=0.7, relwidth=0.15, relheight=0.3)



        # LABELS

        self.label_main = Label(self.frame_1, text='Exportar Clientes para arquivo Json (zipado)', bg = '#dfe3ee',fg='#000000', font=('Calibri', 18, 'bold'))
        self.label_main.place(relx=0.02, rely=0.02)
        self.label_main = Label(self.frame_2, text='Exportar Fornecedores para arquivo Json (zipado)', bg = '#dfe3ee',fg='#000000', font=('Calibri', 18, 'bold'))
        self.label_main.place(relx=0.02, rely=0.02)
        self.label_main = Label(self.frame_3, text='Exportar Produtos para arquivo Json (zipado)', bg = '#dfe3ee',fg='#000000', font=('Calibri', 18, 'bold'))
        self.label_main.place(relx=0.02, rely=0.02)
        self.label_main = Label(self.frame_4, text='Exportar Usuarios para arquivo Json (zipado)', bg = '#dfe3ee',fg='#000000', font=('Calibri', 18, 'bold'))
        self.label_main.place(relx=0.02, rely=0.02)

    def exportar_Clientes(self):
        import zipfile as zip
        import os
        self.select_cadCliente_Exportar()
        filename  = 'clientes.json'
        
        diretorio = 'C:/Users/Leandro/Desktop/Code/P2_topicos/clientes.zip'
        zf = zip.ZipFile(diretorio, 'w') #arquivo zip destino
        zf.write(diretorio)
        zf.close
        
        self.label_exportar_cliente = Label(self.frame_1, text='Exportado com sucesso para:\n '+ diretorio, bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_exportar_cliente.place(relx=0.34, rely=0.5)

    def exportar_Fornecedores(self):
        import zipfile as zip
        import os
        self.select_cadFornecedores_Exportar()
        filename  = 'fornecedores.json'
        
        diretorio = 'C:/Users/Leandro/Desktop/Code/P2_topicos/fornecedores.zip'
        zf = zip.ZipFile(diretorio, 'w') #arquivo zip destino
        zf.write(diretorio)
        zf.close
        
        self.label_exportar_cliente = Label(self.frame_2, text='Exportado com sucesso para:\n '+ diretorio, bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_exportar_cliente.place(relx=0.34, rely=0.5)

    def exportar_Produtos(self):
        import zipfile as zip
        import os
        self.select_cadProdutos_Exportar()
        filename  = 'produtos.json'
        
        diretorio = 'C:/Users/Leandro/Desktop/Code/P2_topicos/produtos.zip'
        zf = zip.ZipFile(diretorio, 'w') #arquivo zip destino
        zf.write(diretorio)
        zf.close
        
        self.label_exportar_cliente = Label(self.frame_3, text='Exportado com sucesso para:\n '+ diretorio, bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_exportar_cliente.place(relx=0.34, rely=0.5)

    def exportar_Usuarios(self):
        import zipfile as zip
        import os
        self.select_cadUsuarios_Exportar()
        filename  = 'usuarios.json'
        
        diretorio = 'C:/Users/Leandro/Desktop/Code/P2_topicos/usuarios.zip'
        zf = zip.ZipFile(diretorio, 'w') #arquivo zip destino
        zf.write(diretorio)
        zf.close
        
        self.label_exportar_cliente = Label(self.frame_4, text='Exportado com sucesso para:\n '+ diretorio, bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_exportar_cliente.place(relx=0.34, rely=0.5)

    def voltarMenuExportar(self):
        self.telaExportar.destroy()

Exportar()