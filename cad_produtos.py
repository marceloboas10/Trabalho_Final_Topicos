from imports import *
from relatorios import *
from funcoes import Funcoes
import tkinter as tk

class Produtos(Funcoes):
    def produtos(self): # Inicialização da classe
        self.teladeProdutos = tk.Toplevel()
        self.telaProdutos()
        self.frames_telaProdutos()
        self.cria_botaoProdutos()
        self.lista_frame2Produtos()
        self.criar_tabela_cadProdutos()
        self.select_cadProdutos()

    def telaProdutos(self):
        self.teladeProdutos.title('Cadastro de Produtos') # Title cria o titulo do Tkinter
        self.teladeProdutos.geometry('980x600') # Tamanho da tela
        self.teladeProdutos.maxsize(width=980, height=600) #Tamanho maximo da tela
        self.teladeProdutos.minsize(width=600, height=460) #Tamanho minimo da tela
        self.teladeProdutos.resizable(True, True) # Tela responsiva
        self.teladeProdutos.configure(background='#1e3743') # Cor de fundo

    def frames_telaProdutos(self):
        self.frame_1 = Frame(self.teladeProdutos, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2 = Frame(self.teladeProdutos, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def cria_botaoProdutos(self):
        # Botão Limpar
        self.botaoLimpar = Button(self.frame_1,text='Limpar',border=2 ,bg='#109db2', fg='white', font = ('verdana', 8, 'bold'), command= self.limpar_telaProdutos)
        self.botaoLimpar.place(relx=0.54, rely=0.8, relwidth=0.1, relheight=0.10, )

        # Botão Buscar
        self.botaoBuscar = Button(self.frame_1, text='Buscar', border=2, bg='#109db2', fg='white', font = ('verdana', 8 , 'bold'), command=self.buscar_produtos)
        self.botaoBuscar.place(relx=0.02, rely=0.8, relwidth=0.1, relheight=0.10)

        # Botão Cadastrar
        self.botaoNovo = Button(self.frame_1, text='Cadastrar', border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command=self.insert_cadProdutos)
        self.botaoNovo.place(relx=0.15, rely=0.8, relwidth=0.1,relheight=0.10)

        # Botão Alterar
        self.botaoAlterar = Button(self.frame_1, text='Alterar',border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command= self.alterar_produtos)
        self.botaoAlterar.place(relx=0.28, rely=0.8, relwidth=0.1, relheight=0.10)

        # Botão Apagar
        self.botaoApagar = Button(self.frame_1, text='Apagar',border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command= self.deleta_produtos)
        self.botaoApagar.place(relx=0.41, rely=0.8, relwidth=0.1, relheight=0.10)

        # Botão Voltar
        self.botaoApagar = Button(self.frame_1, text='Voltar para Menu',border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command= self.voltarMenuProdutos)
        self.botaoApagar.place(relx=0.67, rely=0.8, relwidth=0.15, relheight=0.10)

        # LABELS

        self.label_codigo = Label(self.frame_1, text='CADASTRO DE PRODUTOS', bg = '#dfe3ee',fg='#000000', font=('Calibri', 22, 'bold'))
        self.label_codigo.place(relx=0.02, rely=0.02)

        #Criação do label Código
        self.label_codigo = Label(self.frame_1, text='Código', bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_codigo.place(relx=0.02, rely=0.15)
        self.entry_codigo = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_codigo.place(relx=0.02, rely=0.25, relwidth=0.08, relheight=0.10)

        # Criação do label Produto
        self.label_produto = Label(self.frame_1, text="Produto", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_produto.place(relx=0.12, rely=0.15)
        self.entry_produto = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_produto.place(relx=0.12, rely=0.25, relwidth=0.86, relheight=0.10)

        # Criação do label Marca
        self.label_marca = Label(self.frame_1, text="Marca", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_marca.place(relx=0.02, rely=0.35)
        self.entry_marca = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_marca.place(relx=0.02, rely=0.45, relwidth=0.3, relheight=0.10)

        # Criação do label Fabricante
        self.label_fabricante = Label(self.frame_1, text="Fabricante", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_fabricante.place(relx= 0.66, rely=0.35)
        self.entry_fabricante = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_fabricante.place(relx=0.66, rely=0.45, relwidth=0.32, relheight=0.10)

        # Criação do label Modelo
        self.label_modelo = Label(self.frame_1, text="Modelo", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_modelo.place(relx=0.34, rely=0.35)
        self.entry_modelo = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_modelo.place(relx=0.34, rely=0.45, relwidth=0.3, relheight=0.10)

        # Criação do label Tipo
        self.label_tipo = Label(self.frame_1, text="Tipo", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_tipo.place(relx= 0.02, rely=0.55)
        self.entry_tipo = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_tipo.place(relx=0.02, rely=0.65, relwidth=0.3, relheight=0.10)

        # Criação do label Cód Fornecedor
        self.label_codfornecedor = Label(self.frame_1, text="Código Fornecedor", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_codfornecedor.place(relx= 0.77, rely=0.55)
        self.entry_codfornecedor = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_codfornecedor.place(relx=0.77, rely=0.65, relwidth=0.21, relheight=0.10)

        # Criação do label Sub Tipo
        self.label_subtipo = Label(self.frame_1, text="Sub Tipo", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_subtipo.place(relx=0.34, rely=0.55)
        self.entry_subtipo = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_subtipo.place(relx=0.34, rely=0.65, relwidth=0.3, relheight=0.10)

        # Criação do label Estoque
        self.label_estoque = Label(self.frame_1, text="Estoque", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_estoque.place(relx=0.66, rely=0.55)
        self.entry_estoque = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_estoque.place(relx=0.66, rely=0.65, relwidth=0.09, relheight=0.10)

    # Criação da Treeview
    def lista_frame2Produtos(self):
        self.lista_produtos = ttk.Treeview(self.frame_2, height=3, column=('col1','col2','col3','col4','col5','col6','col7','col8','col9'))
        self.lista_produtos.heading('#1',text='Código')
        self.lista_produtos.heading('#2',text='Produto')
        self.lista_produtos.heading('#3',text='Marca')
        self.lista_produtos.heading('#4', text='Modelo')
        self.lista_produtos.heading('#5',text='Fabricante')
        self.lista_produtos.heading('#6',text='Tipo')
        self.lista_produtos.heading('#7',text='Sub Tipo')
        self.lista_produtos.heading('#8',text='Estoque')
        self.lista_produtos.heading('#9',text='Codigo Fornecedor')
        

        # Tamanho das colunas em relação ao quadro (quadro tem 500)
        self.lista_produtos.column('#0',width=1)
        self.lista_produtos.column('#1',width=35)
        self.lista_produtos.column('#2',widt=100)
        self.lista_produtos.column('#3',width=55)
        self.lista_produtos.column('#4',width=110)
        self.lista_produtos.column('#5',width=70)
        self.lista_produtos.column('#6',width=40)
        self.lista_produtos.column('#7',width=85)
        self.lista_produtos.column('#8',width=50)
        self.lista_produtos.column('#9',width=100)


        # Criação da lista
        self.lista_produtos.place(relx=0.01,rely=0.1, relwidth=0.95, relheight=0.85)

        # Barra de rolagem lateral
        self.scrollLista = Scrollbar(self.frame_2, orient='vertical')
        self.lista_produtos.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.lista_produtos.bind('<Double-1>', self.duplo_clickProdutos)

    def voltarMenuProdutos(self):
        self.teladeProdutos.destroy()

Produtos()