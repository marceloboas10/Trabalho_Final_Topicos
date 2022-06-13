from imports import *


class Funcoes():
    # Função para limpar os dados dos campos da tela do Cadastro de Clientes
    def limpar_telaClientes(self):
        self.entry_codigo.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_endereco.delete(0, END)
        self.entry_complemento.delete(0,END)
        self.entry_numero.delete(0, END)
        self.entry_bairro.delete(0, END)
        self.entry_cep.delete(0, END)
        self.entry_cidade.delete(0, END)
        self.entry_telefone.delete(0, END)
        self.entry_estado.delete(0, END)
    
    # Função para limpar os dados dos campos da tela de Usuários
    def limpar_telaUsuarios(self):
        self.entry_nomeuser.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_senha1.delete(0, END)
        self.entry_senha2.delete(0,END)

    # Função para limpar os dados dos campos da tela de Gerar Pedidos
    def limpar_telaGera_Pedidos(self):
        self.entry_codigo_cliente.delete(0, END)
        self.entry_nome_cliente.delete(0, END)


    # Função para limpar os dados dos campos da tela do Cadastro de Produtos
    def limpar_telaProdutos(self):
        self.entry_codigo.delete(0, END)
        self.entry_produto.delete(0, END)
        self.entry_marca.delete(0, END)
        self.entry_fabricante.delete(0,END)
        self.entry_modelo.delete(0, END)
        self.entry_tipo.delete(0, END)
        self.entry_subtipo.delete(0, END)
        self.entry_estoque.delete(0, END)
        self.entry_codfornecedor.delete(0, END)

    # Função para limpar os dados dos campos da tela do Cadastro de Fornecedores
    def limpar_telaFornecedores(self):
        self.entry_codigo.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_endereco.delete(0, END)
        self.entry_complemento.delete(0,END)
        self.entry_numero.delete(0, END)
        self.entry_bairro.delete(0, END)
        self.entry_cep.delete(0, END)
        self.entry_cidade.delete(0, END)
        self.entry_telefone.delete(0, END)
        self.entry_estado.delete(0, END)

    # Criação do banco de dados SqlLite
    def conectar_sql(self):
        self.conecta_db = sqlite3.connect('banco.bd')
        self.cursor = self.conecta_db.cursor()
        print('Conectando ao banco Clientes')

    # Desconecta do banco de dados
    def desconecta_sql(self):
        self.conecta_db.close()
        print('Desconectando ao bando de dados')

    # Montar as tabelas Sqlite de Clientes
    def criar_tabela_cadCliente(self):
        self.conectar_sql()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                codigo INTEGER PRIMARY KEY,
                nome CHAR(40) NOT NULL,
                endereco CHAR(50),
                complemento CHAR,
                numero INTEGER,
                bairro CHAR(20),
                telefone INTEGER,
                cep INTEGER,
                cidade CHAR(40),
                estado CHAR(2)
            );
        """)

        self.conecta_db.commit(); print('Tabela de clientes criada')
        self.desconecta_sql()

    # Montar as tabelas Sqlite de Produtos
    def criar_tabela_cadProdutos(self):
        self.conectar_sql()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                codigo INTEGER PRIMARY KEY,
                produto CHAR(40) NOT NULL,
                marca CHAR(30),
                fabricante CHAR(30),
                modelo CHAR(30),
                tipo CHAR(30),
                subtipo CHAR(30),
                estoque INTEGER,
                codfornecedor CHAR(15)
            );
        """)

        self.conecta_db.commit(); print('Tabela de produtos criada')
        self.desconecta_sql()

    # Montar as tabelas Sqlite de Fornecedores
    def criar_tabela_cadFornecedores(self):
        self.conectar_sql()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS fornecedores (
                codigo INTEGER PRIMARY KEY,
                nome CHAR(40) NOT NULL,
                endereco CHAR(50),
                complemento CHAR,
                numero INTEGER,
                bairro CHAR(20),
                telefone INTEGER,
                cep INTEGER,
                cidade CHAR(40),
                estado CHAR(2)
            );
        """)
        self.conecta_db.commit(); print('Tabela de fornecedores criada')
        self.desconecta_sql()

    # Montar as tabelas Sqlite de Usuarios
    def criar_tabela_cadUsuarios(self):
        self.conectar_sql()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                nomeuser CHAR(50) PRIMARY KEY,
                email CHAR(40),
                senha CHAR(40)
            );
        """)
        self.conecta_db.commit(); print('Tabela de usuarios criada')
        self.desconecta_sql()

    def criar_tabela_geraPedidos(self):
        self.conectar_sql()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedidos (
                pedido INTEGER PRIMARY KEY,
                cod_cliente INTEGER,
                nome_cliente CHAR(50),
                cod_produto INTEGER,
                nome_produto CHAR(50),
                marca_produto CHAR(40),
                modelo_produto CHAR(40),
                fabricante_produto CHAR(40),
                qtde INTEGER,
                tipo_pagto CHAR(30),
                tipo_transporte CHAR(30)
            );
        """)
        self.conecta_db.commit(); print('Tabela de pedidos criada')
        self.desconecta_sql()


    # Criacao variaveis tela Cadastro Clientes
    def variaveis_cadCliente(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.telefone = self.entry_telefone.get()
        self.cidade = self.entry_cidade.get()
        self.endereco = self.entry_endereco.get()
        self.complemento = self.entry_complemento.get()
        self.numero = self.entry_numero.get()
        self.bairro = self.entry_bairro.get()
        self.estado = self.entry_estado.get()
        self.cep = self.entry_cep.get()
    
    # Criacao variaveis tela Cadastro Usuarios
    def variaveis_cadUsuario(self):
        self.nome_usuario = self.entry_nomeuser.get()
        self.senha = self.entry_senha1.get()
        self.email = self.entry_email.get()
    
    # Criacao variaveis tela Cadastro Produtos
    def variaveis_cadProdutos(self):
        self.codigo = self.entry_codigo.get()
        self.produto = self.entry_produto.get()
        self.marca = self.entry_marca.get()
        self.fabricante = self.entry_fabricante.get()
        self.modelo = self.entry_modelo.get()
        self.tipo = self.entry_tipo.get()
        self.subtipo = self.entry_subtipo.get()
        self.estoque = self.entry_estoque.get()
        self.codfornecedor = self.entry_codfornecedor.get()
    
    # Criacao variaveis tela Cadastro Fornecedores
    def variaveis_cadFornecedores(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.telefone = self.entry_telefone.get()
        self.cidade = self.entry_cidade.get()
        self.endereco = self.entry_endereco.get()
        self.complemento = self.entry_complemento.get()
        self.numero = self.entry_numero.get()
        self.bairro = self.entry_bairro.get()
        self.estado = self.entry_estado.get()
        self.cep = self.entry_cep.get()
        
    # Função Insert dados Banco de Dados - Clientes
    def insert_cadCliente(self):
        self.variaveis_cadCliente()
        
        # Aviso se o nome estiver em branco
        if self.entry_nome.get() == '':
            msg = "PARA CADASTRAR UM CLIENTE INSIRA UM NOME"
            messagebox.showinfo('AVISO!!! - Cadasdro de Clientes ', msg)
        else:
            self.conectar_sql()
            self.cursor.execute(""" INSERT INTO clientes ( nome, endereco, complemento, numero, bairro, telefone, cep, cidade, estado)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (self.nome, self.endereco, self.complemento, self.numero, self.bairro , self.telefone, self.cep, self.cidade, self.estado))
            self.conecta_db.commit()
            self.desconecta_sql()
            self.select_cadCliente()
            self.limpar_telaClientes()

    # Função Insert dados Banco de Dados - Usuarios
    def insert_cadUsuario(self):
        self.variaveis_cadUsuario()        
        # Aviso se o nome estiver em branco

        if self.entry_nomeuser.get() == '':
            msg = "PARA CADASTRAR UM USUARIO INSIRA UM NOME"
            messagebox.showinfo('AVISO!!! - Cadastro de Usuarios ', msg)
        else:
            self.conectar_sql()
            self.cursor.execute(""" INSERT INTO usuarios (nomeuser, email, senha)
                VALUES (?, ?, ?)""", (self.nome_usuario, self.email, self.senha))
            self.conecta_db.commit()
            self.desconecta_sql()
            self.select_cadUsuario()
            self.limpar_telaUsuarios()

    # Função Insert dados Banco de Dados - Clientes
    def insert_cadProdutos(self):
        self.variaveis_cadProdutos()
        
        # Aviso se o nome estiver em branco
        if self.entry_produto.get() == '':
            msg = "PARA CADASTRAR UM PRODUTO, INSIRA UM NOME"
            messagebox.showinfo('AVISO!!! - Cadastro de Produtos ', msg)
        else:
            self.conectar_sql()
            self.cursor.execute(""" INSERT INTO produtos ( codigo, produto, marca, fabricante, modelo, tipo, subtipo, estoque, codfornecedor)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (self.codigo, self.produto, self.marca, self.fabricante, self.modelo, self.tipo , self.subtipo, self.estoque, self.codfornecedor))
            self.conecta_db.commit()
            self.desconecta_sql()
            self.select_cadProdutos()
            self.limpar_telaProdutos()

    # Função Insert dados Banco de Dados - Fornecedores
    def insert_cadFornecedores(self):
        self.variaveis_cadFornecedores()
        
        # Aviso se o nome estiver em branco
        if self.entry_nome.get() == '':
            msg = "PARA CADASTRAR UM FORNECEDOR, INSIRA UM NOME"
            messagebox.showinfo('AVISO!!! - Cadasdro de Fornecedores ', msg)
        else:
            self.conectar_sql()
            self.cursor.execute(""" INSERT INTO fornecedores (nome, endereco, complemento, numero, bairro, telefone, cep, cidade, estado)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (self.nome, self.endereco, self.complemento, self.numero, self.bairro , self.telefone, self.cep, self.cidade, self.estado))
            self.conecta_db.commit()
            self.desconecta_sql()
            self.select_cadFornecedores()
            self.limpar_telaFornecedores()

    #INSERT SENHA PADRÃO INICIO
    def insert_Padrao(self):
        self.conectar_sql()
        self.cursor.execute(""" INSERT INTO usuarios (nomeuser, email, senha)
            VALUES (?, ?, ?)""", ("Admin", "admin@admin", "masteradmin"))
        self.conecta_db.commit()
        self.desconecta_sql()

    # Função Select Banco de Dados Clientes
    def select_cadCliente(self):
        self.lista_menu.delete(*self.lista_menu.get_children())
        self.conectar_sql()
        lista = self.cursor.execute(""" SELECT codigo, nome, telefone, endereco, complemento, numero, bairro, cep, cidade, estado FROM clientes
            ORDER BY nome, codigo ASC; """)
        for i in lista:
            self.lista_menu.insert("", END, values=i)
        self.desconecta_sql()

    # Função Select Banco de Dados Clientes para Exportar Json
    def select_cadCliente_Exportar(self):
        import json
        import os
        self.conectar_sql()
        lista = self.cursor.execute(""" SELECT codigo, nome, telefone, endereco, complemento, numero, bairro, cep, cidade, estado FROM clientes
            ORDER BY nome, codigo ASC; """)
        banco = self.cursor.fetchall()
        lista = []
        for i in banco:
            lista.append({
                'codigo': i[0],
                'nome'  : i[1],
                'telefone' : i[2],
                'endereco' : i[3],
                'complemento' : i[4],
                'numero' : i[5],
                'bairro' : i[6],
                'cep' : i[7],
                'cidade' : i[8],
                'estado' : i[9]
        })
        diretorio = 'C:/Users/Leandro/Desktop/Code/P2_topicos/clientes.json'
        f = open(diretorio, "w", encoding="iso-8859-1")
        json.dump(lista, f, sort_keys=True, indent=4)
        f.close()

        self.desconecta_sql()

    # Função Select Banco de Dados Fornecedores para Exportar Json
    def select_cadFornecedores_Exportar(self):
        import json
        self.conectar_sql()
        lista = self.cursor.execute(""" SELECT codigo, nome, telefone, endereco, complemento, numero, bairro, cep, cidade, estado FROM fornecedores
            ORDER BY nome, codigo ASC; """)
        banco = self.cursor.fetchall()
        lista = []
        for i in banco:
            lista.append({
                'codigo': i[0],
                'nome'  : i[1],
                'telefone' : i[2],
                'endereco' : i[3],
                'complemento' : i[4],
                'numero' : i[5],
                'bairro' : i[6],
                'cep' : i[7],
                'cidade' : i[8],
                'estado' : i[9]
        })
        diretorio = 'C:/Users/Leandro/Desktop/Code/P2_topicos/fornecedores.json'
        f = open(diretorio, "w", encoding="iso-8859-1")
        json.dump(lista, f, sort_keys=True, indent=4)
        f.close()

        self.desconecta_sql()

    # Função Select Banco de Dados Produtos para Exportar Json
    def select_cadProdutos_Exportar(self):
        import json
        self.conectar_sql()
        lista = self.cursor.execute(""" SELECT codigo, produto, marca, fabricante, modelo, tipo, subtipo, estoque, codfornecedor FROM produtos
            ORDER BY produto, codigo ASC; """)
        banco = self.cursor.fetchall()
        lista = []
        for i in banco:
            lista.append({
                'codigo': i[0],
                'produto'  : i[1],
                'marca' : i[2],
                'fabricante' : i[3],
                'modelo' : i[4],
                'tipo' : i[5],
                'subtipo' : i[6],
                'estoque' : i[7],
                'codfornecedor' : i[8]
        })
        diretorio = 'C:/Users/Leandro/Desktop/Code/P2_topicos/produtos.json'
        f = open(diretorio, "w", encoding="iso-8859-1")
        json.dump(lista, f, sort_keys=True, indent=4)
        f.close()

        self.desconecta_sql()

    # Função Select Banco de Dados Usuarios para Exportar Json
    def select_cadUsuarios_Exportar(self):
        import json
        self.conectar_sql()
        lista = self.cursor.execute(""" SELECT nomeuser, email, senha FROM usuarios
            ORDER BY nomeuser ASC; """)
        banco = self.cursor.fetchall()
        lista = []
        for i in banco:
            lista.append({
                'nomeuser': i[0],
                'email'  : i[1],
                'senha' : i[2]
        })
        diretorio = 'C:/Users/Leandro/Desktop/Code/P2_topicos/usuarios.json'
        f = open(diretorio, "w", encoding="iso-8859-1")
        json.dump(lista, f, sort_keys=True, indent=4)
        f.close()

        self.desconecta_sql()

    # Função Select Banco de Dados Usuarios
    def select_cadUsuario(self):
        self.lista_menu_users.delete(*self.lista_menu_users.get_children())
        self.conectar_sql()
        lista = self.cursor.execute(""" SELECT nomeuser, email, senha FROM usuarios
            ORDER BY nomeuser ASC; """)
        for i in lista:
            self.lista_menu_users.insert("", END, values=i)
        self.desconecta_sql()
    
    # Função Select Banco de Dados Produtos
    def select_cadProdutos(self):
        self.lista_produtos.delete(*self.lista_produtos.get_children())
        self.conectar_sql()
        lista = self.cursor.execute(""" SELECT codigo, produto, marca, fabricante, modelo, tipo, subtipo, estoque, codfornecedor FROM produtos
            ORDER BY produto, codigo ASC; """)
        for i in lista:
            self.lista_produtos.insert("", END, values=i)
        self.desconecta_sql()

    # Função Select Banco de Dados Fornecedores
    def select_cadFornecedores(self):
        self.lista_fornecedores.delete(*self.lista_fornecedores.get_children())
        self.conectar_sql()
        lista = self.cursor.execute(""" SELECT codigo, nome, telefone, endereco, complemento, numero, bairro, cep, cidade, estado FROM fornecedores
            ORDER BY nome, codigo ASC; """)
        for i in lista:
            self.lista_fornecedores.insert("", END, values=i)
        self.desconecta_sql()
        

    # Apagar com duplo clique Clientes
    def duplo_clickClientes(self, event):
        self.limpar_telaClientes()
        self.lista_menu.selection()

        for n in self.lista_menu.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = self.lista_menu.item(n, 'values')
            self.entry_codigo.insert(END, col1)
            self.entry_nome.insert(END, col2)
            self.entry_telefone.insert(END, col3)
            self.entry_endereco.insert(END, col4)
            self.entry_complemento.insert(END, col5)
            self.entry_numero.insert(END, col6)
            self.entry_bairro.insert(END, col7)
            self.entry_cep.insert(END, col8)
            self.entry_cidade.insert(END, col9)
            self.entry_estado.insert(END, col10)

    # Apagar com duplo clique Usuarios
    def duplo_clickUsuarios(self, event):
        self.limpar_telaUsuarios()
        self.lista_menu_users.selection()

        for i in self.lista_menu_users.selection():
            col1, col2, col3 = self.lista_menu_users.item(i, 'values')
            self.entry_nomeuser.insert(END, col1)
            self.entry_email.insert(END, col2)
            self.entry_senha1.insert(END, col3)
            self.entry_senha2.insert(END, col3)
    
    # Apagar com duplo clique Produtos
    def duplo_clickProdutos(self, event):
        self.limpar_telaProdutos()
        self.lista_produtos.selection()

        for n in self.lista_produtos.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.lista_produtos.item(n, 'values')
            self.entry_codigo.insert(END, col1)
            self.entry_produto.insert(END, col2)
            self.entry_marca.insert(END, col3)
            self.entry_modelo.insert(END, col4)
            self.entry_fabricante.insert(END, col5)
            self.entry_tipo.insert(END, col6)
            self.entry_subtipo.insert(END, col7)
            self.entry_estoque.insert(END, col8)
            self.entry_codfornecedor.insert(END, col9)

     # Apagar com duplo clique Fornecedores
    def duplo_clickFornecedores(self, event):
        self.limpar_telaFornecedores()
        self.lista_fornecedores.selection()

        for n in self.lista_fornecedores.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = self.lista_fornecedores.item(n, 'values')
            self.entry_codigo.insert(END, col1)
            self.entry_nome.insert(END, col2)
            self.entry_telefone.insert(END, col3)
            self.entry_endereco.insert(END, col4)
            self.entry_complemento.insert(END, col5)
            self.entry_numero.insert(END, col6)
            self.entry_bairro.insert(END, col7)
            self.entry_cep.insert(END, col8)
            self.entry_cidade.insert(END, col9)
            self.entry_estado.insert(END, col10)
    
    def duplo_clickPClientes(self, event):
        for n in self.listaclientes.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = self.listaclientes.item(n, 'values')
            self.entry_codigo_cliente.insert(END, col1)
            self.entry_nome_cliente.insert(END, col2)
      

    # Deleta cliente
    def deleta_clientes(self):
        self.variaveis_cadCliente()
        self.conectar_sql()
        self.cursor.execute(""" DELETE FROM clientes WHERE codigo = ? """, (self.codigo,))
        self.conecta_db.commit()
        self.desconecta_sql()
        self.limpar_telaClientes()
        self.select_cadCliente()
    
    # Deleta usuario
    def deleta_usuarios(self):
        self.variaveis_cadUsuario()
        self.conectar_sql()
        self.cursor.execute(""" DELETE FROM usuarios WHERE nomeuser = ? """, (self.nome_usuario,))
        self.conecta_db.commit()
        self.desconecta_sql()
        self.limpar_telaUsuarios()
        self.select_cadUsuario()

     # Deleta produtos
    def deleta_produtos(self):
        self.variaveis_cadProdutos()
        self.conectar_sql()
        self.cursor.execute(""" DELETE FROM produtos WHERE codigo = ? """, (self.codigo,))
        self.conecta_db.commit()
        self.desconecta_sql()
        self.limpar_telaProdutos()
        self.select_cadProdutos()

    # Deleta fornecedores
    def deleta_fornecedores(self):
        self.variaveis_cadFornecedores()
        self.conectar_sql()
        self.cursor.execute(""" DELETE FROM fornecedores WHERE codigo = ? """, (self.codigo,))
        self.conecta_db.commit()
        self.desconecta_sql()
        self.limpar_telaFornecedores()
        self.select_cadFornecedores()

    # Alterar clientes
    def alterar_cliente(self):
        self.variaveis_cadCliente()
        self.conectar_sql()
        self.cursor.execute(""" UPDATE clientes SET nome = ?, telefone = ?, cidade = ?, complemento = ?, numero = ?,
            bairro = ?, estado = ? WHERE codigo = ? """,
            (self.nome, self.telefone, self.cidade, self.complemento, self.numero, self.bairro, self.estado, self.codigo))
        self.conecta_db.commit()
        self.desconecta_sql()
        self.limpar_telaClientes()
        self.select_cadCliente()
    
    # Alterar usuarios
    def alterar_usuario(self):
        self.variaveis_cadUsuario()
        self.conectar_sql()
        self.cursor.execute(""" UPDATE usuarios SET nomeuser = ?, email = ?, senha = ?""",
            (self.nome_usuario, self.email, self.senha))
        self.conecta_db.commit()
        self.desconecta_sql()
        self.limpar_telaUsuarios()
        self.select_cadUsuario()

    # Alterar produtos
    def alterar_produtos(self):
        self.variaveis_cadProdutos()
        self.conectar_sql()
        self.cursor.execute(""" UPDATE produtos SET produto = ?, marca = ?, fabricante = ?, modelo = ?, tipo = ?,
            subtipo = ?, estoque = ? WHERE codigo = ? """,
            (self.produto, self.marca, self.fabricante, self.modelo, self.tipo, self.subtipo, self.estoque, self.codigo))
        self.conecta_db.commit()
        self.desconecta_sql()
        self.limpar_telaProdutos()
        self.select_cadProdutos()

    # Alterar fornecedores
    def alterar_fornecedores(self):
        self.variaveis_cadFornecedores()
        self.conectar_sql()
        self.cursor.execute(""" UPDATE fornecedores SET nome = ?, telefone = ?, cidade = ?, complemento = ?, numero = ?,
            bairro = ?, estado = ? WHERE codigo = ? """,
            (self.nome, self.telefone, self.cidade, self.complemento, self.numero, self.bairro, self.estado, self.codigo))
        self.conecta_db.commit()
        self.desconecta_sql()
        self.limpar_telaFornecedores()
        self.select_cadFornecedores()

    # Buscar clientes
    def buscar_cliente(self):
        self.conectar_sql()
        self.lista_menu.delete(*self.lista_menu.get_children())
        self.entry_nome.insert(END, '%')
        nome = self.entry_nome.get()
        self.cursor.execute(
            """ SELECT codigo, nome, telefone, endereco, complemento, numero, bairro, cep, cidade, estado FROM clientes
            WHERE nome LIKE '%s' ORDER BY nome ASC""" %nome)
        buscaBD = self.cursor.fetchall()
        self.desconecta_sql()
        for i in buscaBD:
            self.lista_menu.insert('', END, values = i)
        self.limpar_telaClientes()
        

    # Buscar usuarios
    def buscar_usuario(self):
        self.conectar_sql()
        self.lista_menu_users.delete(*self.lista_menu.get_children())
        self.entry_nomeuser.insert(END, '%')
        nomeuser = self.entry_nomeuser.get()
        self.cursor.execute(
            """ SELECT nomeuser, email, senha FROM usuarios
            WHERE nomeuser LIKE '%s' ORDER BY nomeuser ASC""" %nomeuser)
        buscaBD = self.cursor.fetchall()
        for i in buscaBD:
            self.lista_menu_users.insert('', END, values = i)
        self.limpar_telaUsuarios()
        self.desconecta_sql

    # Buscar produtos
    def buscar_produtos(self):
        self.conectar_sql()
        self.lista_produtos.delete(*self.lista_produtos.get_children())
        self.entry_produto.insert(END, '%')
        produto = self.entry_produto.get()
        self.cursor.execute(
            """ SELECT codigo, produto, marca, fabricante, modelo, tipo, subtipo, estoque, codfornecedor FROM produtos
            WHERE produto LIKE '%s' ORDER BY produto ASC""" %produto)
        buscaBD = self.cursor.fetchall()
        for i in buscaBD:
            self.lista_produtos.insert('', END, values = i)
        self.limpar_telaProdutos()
        self.desconecta_sql

    # Buscar fornecedores
    def buscar_fornecedores(self):
        self.conectar_sql()
        self.lista_fornecedores.delete(*self.lista_fornecedores.get_children())
        self.entry_nome.insert(END, '%')
        nome = self.entry_nome.get()
        self.cursor.execute(
            """ SELECT codigo, nome, telefone, cidade, endereco, complemento, numero, bairro, cep, estado FROM fornecedores
            WHERE nome LIKE '%s' ORDER BY nome ASC""" %nome)
        buscaBD = self.cursor.fetchall()
        for i in buscaBD:
            self.lista_fornecedores.insert('', END, values = i)
        self.limpar_telaFornecedores()
        self.desconecta_sql

    #Buscar cliente para gerar pedido
    def buscar_cliente_Pedido(self):
        self.conectar_sql()
        self.listaclientes.delete(*self.listaclientes.get_children())
        self.entry_nome_cliente.insert(END, '%')
        nome = self.entry_nome_cliente.get()
        self.cursor.execute(
            """ SELECT codigo, nome, telefone, endereco, complemento, numero, bairro, cep, cidade, estado FROM clientes
            WHERE nome LIKE '%s' ORDER BY nome ASC""" %nome)
        busca = self.cursor.fetchall()
        self.desconecta_sql()
        for x in busca:
            self.listaclientes.insert('', END, values = x)
        self.limpar_telaGera_Pedidos()
        # self.desconecta_sql

    