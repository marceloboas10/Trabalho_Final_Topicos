from imports import *
from relatorios import *
from funcoes import Funcoes
import tkinter as tk

class Clientes(Funcoes,Relatorios):
    def clientes(self): # Inicialização da classe
        self.telaClientes = tk.Toplevel()
        self.tela_Clientes()
        self.frames_tela_Clientes()
        self.cria_botao_Clientes()
        self.lista_frame2_Clientes()
        self.criar_tabela_cadCliente()
        self.select_cadCliente()
        #telaClientes.mainloop() # Criar um loop para abrir a janela        

    def cepCorreios(self):
        try:
            self.entry_cidade.delete(0, END)
            self.entry_bairro.delete(0, END)
            self.entry_endereco.delete(0, END)
            self.entry_complemento.delete(0, END)
            self.entry_estado.delete(0, END)
            zipcode = self.entry_cep.get()
            dadosCep = pycep_correios.get_address_from_cep(zipcode)
            print(dadosCep)
            self.entry_endereco.insert(END, dadosCep['logradouro'])
            self.entry_complemento.insert(END, dadosCep['complemento'])
            self.entry_bairro.insert(END, dadosCep['bairro'])
            self.entry_cidade.insert(END, dadosCep['cidade'])
            self.entry_estado.insert(END, dadosCep['uf'])
        except:
            messagebox.showinfo('Erro Sistema', 'CEP INEXISTENTE')


    def tela_Clientes(self):
        self.telaClientes.title('Cadastro de Clientes') # Title cria o titulo do Tkinter
        self.telaClientes.geometry('980x600') # Tamanho da tela
        self.telaClientes.maxsize(width=980, height=600) #Tamanho maximo da tela
        self.telaClientes.minsize(width=600, height=460) #Tamanho minimo da tela
        self.telaClientes.resizable(False, False) # Tela responsiva
        self.telaClientes.configure(background='#1e3743') # Cor de fundo

    def frames_tela_Clientes(self):
        self.frame_1 = Frame(self.telaClientes, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2 = Frame(self.telaClientes, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def cria_botao_Clientes(self):
        # Botão Limpar
        self.botaoLimpar = Button(self.frame_1,text='Limpar',border=2 ,bg='#109db2', fg='white', font = ('verdana', 8, 'bold'), command= self.limpar_telaClientes)
        self.botaoLimpar.place(relx=0.54, rely=0.8, relwidth=0.1, relheight=0.10, )

        # Botão Buscar
        self.botaoBuscar = Button(self.frame_1, text='Buscar', border=2, bg='#109db2', fg='white', font = ('verdana', 8 , 'bold'), command=self.buscar_cliente)
        self.botaoBuscar.place(relx=0.02, rely=0.8, relwidth=0.1, relheight=0.10)

        # Botão Cadastrar
        self.botaoNovo = Button(self.frame_1, text='Cadastrar', border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command=self.insert_cadCliente)
        self.botaoNovo.place(relx=0.15, rely=0.8, relwidth=0.1,relheight=0.10)

        # Botão Salvar
        self.botaoAlterar = Button(self.frame_1, text='Salvar',border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command= self.alterar_cliente)
        self.botaoAlterar.place(relx=0.28, rely=0.8, relwidth=0.1, relheight=0.10)

        # Botão Apagar
        self.botaoApagar = Button(self.frame_1, text='Apagar',border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command= self.deleta_clientes)
        self.botaoApagar.place(relx=0.41, rely=0.8, relwidth=0.1, relheight=0.10)

        # Botão Voltar
        self.botaoApagar = Button(self.frame_1, text='Voltar para Menu',border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command=self.voltarMenuClientes)
        self.botaoApagar.place(relx=0.67, rely=0.8, relwidth=0.15, relheight=0.10)

        # Botão Relatório
        self.botaoApagar = Button(self.frame_1, text='Ficha do Cliente',border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command=self.geraRelatorio)
        self.botaoApagar.place(relx=0.85, rely=0.8, relwidth=0.12, relheight=0.10)

        # Botão CEP
        self.botaoCEP = Button(self.frame_1, text='CEP', border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command=self.cepCorreios)
        self.botaoCEP.place(relx=0.74, rely=0.25, relwidth=0.07,relheight=0.10)

        # LABELS

        self.label_codigo = Label(self.frame_1, text='CADASTRO DE CLIENTES', bg = '#dfe3ee',fg='#000000', font=('Calibri', 22, 'bold'))
        self.label_codigo.place(relx=0.02, rely=0.02)

        #Criação do label Código
        self.label_codigo = Label(self.frame_1, text='Código', bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_codigo.place(relx=0.02, rely=0.15)
        self.entry_codigo = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_codigo.place(relx=0.02, rely=0.25, relwidth=0.08, relheight=0.10)

        # self.entry_email = Entry(self.frame, font=('calibri', 14, 'bold'))
        # self.entry_email.place(relx=0.02, rely=0.25, relwidth=0.5,  relheight=0.05)

        # Criação do label Nome
        self.label_nome = Label(self.frame_1, text="Nome do Cliente:", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_nome.place(relx=0.12, rely=0.15)
        self.entry_nome = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_nome.place(relx=0.12, rely=0.25, relwidth=0.6, relheight=0.10)

        # Criação do label endereço
        self.label_endereco = Label(self.frame_1, text="Endereço", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_endereco.place(relx=0.02, rely=0.35)
        self.entry_endereco = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_endereco.place(relx=0.02, rely=0.45, relwidth=0.6, relheight=0.10)

        # Criação do label complemento
        self.label_complemento = Label(self.frame_1, text="Complemento", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_complemento.place(relx= 0.76, rely=0.35)
        self.entry_complemento = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_complemento.place(relx=0.76, rely=0.45, relwidth=0.22, relheight=0.10)

        # Criação do label numero residencia
        self.label_numero = Label(self.frame_1, text="Número", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_numero.place(relx=0.64, rely=0.35)
        self.entry_numero = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_numero.place(relx=0.64, rely=0.45, relwidth=0.10, relheight=0.10)

        # Criação do label bairro
        self.label_bairro = Label(self.frame_1, text="Bairro", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_bairro.place(relx= 0.02, rely=0.55)
        self.entry_bairro = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_bairro.place(relx=0.02, rely=0.65, relwidth=0.4, relheight=0.10)

        # Criação do label Telefone
        self.label_telefone = Label(self.frame_1, text="Telefone", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_telefone.place(relx= 0.77, rely=0.55)
        self.entry_telefone = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_telefone.place(relx=0.77, rely=0.65, relwidth=0.21, relheight=0.10)
        
        
        # Criação label CEP
        self.label_cep = Label(self.frame_1, text="CEP", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_cep.place(relx= 0.83, rely=0.15)
        self.entry_cep = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_cep.place(relx=0.83, rely=0.25, relwidth=0.15, relheight=0.10)

        # Criação do label Cidade
        self.label_cidade = Label(self.frame_1, text="Cidade", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_cidade.place(relx=0.44, rely=0.55)
        self.entry_cidade = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_cidade.place(relx=0.44, rely=0.65, relwidth=0.25, relheight=0.10)

        # Criação do label Estado
        self.label_estado = Label(self.frame_1, text="UF", bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.label_estado.place(relx=0.71, rely=0.55)
        self.entry_estado = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.entry_estado.place(relx=0.71, rely=0.65, relwidth=0.04, relheight=0.10)

    # Criação da Treeview
    def lista_frame2_Clientes(self):
        self.lista_menu = ttk.Treeview(self.frame_2, height=3, column=('col1','col2','col3','col4','col5','col6','col7','col8','col9','col10'))
        self.lista_menu.heading('#1',text='Código')
        self.lista_menu.heading('#2',text='Nome')
        self.lista_menu.heading('#3',text='Telefone')
        self.lista_menu.heading('#4', text='Endereço')
        self.lista_menu.heading('#5',text='Complemento')
        self.lista_menu.heading('#6',text='Número')
        self.lista_menu.heading('#7',text='Bairro')
        self.lista_menu.heading('#8',text='CEP')
        self.lista_menu.heading('#9',text='Cidade')
        self.lista_menu.heading('#10',text='Estado')
        

        # Tamanho das colunas em relação ao quadro (quadro tem 500)
        self.lista_menu.column('#0',width=1)
        self.lista_menu.column('#1',width=35)
        self.lista_menu.column('#2',widt=100)
        self.lista_menu.column('#3',width=55)
        self.lista_menu.column('#4',width=110)
        self.lista_menu.column('#5',width=70)
        self.lista_menu.column('#6',width=40)
        self.lista_menu.column('#7',width=85)
        self.lista_menu.column('#8',width=50)
        self.lista_menu.column('#9',width=100)
        self.lista_menu.column('#10',width=30)

        # Criação da lista
        self.lista_menu.place(relx=0.01,rely=0.1, relwidth=0.95, relheight=0.85)

        # Barra de rolagem lateral
        self.scrollLista = Scrollbar(self.frame_2, orient='vertical')
        self.lista_menu.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.lista_menu.bind('<Double-1>', self.duplo_clickClientes)
    
    def voltarMenuClientes(self):
        self.telaClientes.destroy()

Clientes()