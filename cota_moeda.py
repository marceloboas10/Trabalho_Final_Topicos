from imports import *
from funcoes import Funcoes

import tkinter as tk

class Moeda(Funcoes):
    def moeda(self): # Inicialização da classe
        self.telaMoeda = tk.Toplevel()
        self.tela_moeda()
        self.frames_telaMoeda()
        self.cria_botoes()
        self.cotaDolar()
        self.cotaEuro()
        self.cotaBTC()

    def tela_moeda(self):
        self.telaMoeda.title('Conversão de Moedas') # Title cria o titulo do Tkinter
        self.telaMoeda.geometry('980x600') # Tamanho da tela
        self.telaMoeda.maxsize(width=980, height=600) #Tamanho maximo da tela
        self.telaMoeda.minsize(width=600, height=460) #Tamanho minimo da tela
        self.telaMoeda.configure(background='#1e3743') # Cor de fundo

    def frames_telaMoeda(self):
        self.frame_1 = Frame(self.telaMoeda, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.31, relheight=0.96)
        self.frame_2 = Frame(self.telaMoeda, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_2.place(relx=0.34, rely=0.02, relwidth=0.31, relheight=0.96)
        self.frame_3 = Frame(self.telaMoeda, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_3.place(relx=0.66, rely=0.02, relwidth=0.31, relheight=0.96)

    def cria_botoes(self):
        # LABELS

        self.label_main = Label(self.frame_1, text='US$ Dollar', bg = '#dfe3ee',fg='#000000', font=('Calibri', 22, 'bold'))
        self.label_main.place(relx=0.02, rely=0.002)

        self.label_main = Label(self.frame_2, text='Euro', bg = '#dfe3ee',fg='#000000', font=('Calibri', 22, 'bold'))
        self.label_main.place(relx=0.02, rely=0.002)

        self.label_main = Label(self.frame_3, text='Bit Coin', bg = '#dfe3ee',fg='#000000', font=('Calibri', 22, 'bold'))
        self.label_main.place(relx=0.02, rely=0.002)

        # Botão Voltar
        self.botaoVoltar = Button(self.frame_3, text='Voltar para Menu',border=2,bg='#109db2', fg='white', font=('verdana', 8, 'bold'), command= self.voltarMenuCota)
        self.botaoVoltar.place(relx=0.6, rely=0.9, relwidth=0.4, relheight=0.07)


    def cotaDolar(self):
        import requests
        import json
        requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
        cotacao = requisicao.json()
        
        data = ('Data e Hora da Cotação: \n' + cotacao['USD']['create_date'])

        self.Valor_dolar = round(float(cotacao['USD']['bid']),2)

        valordolar = str(self.Valor_dolar).replace(".",",")

        dolar = ('Valor atual: R$ ' + valordolar)

        self.labelDolar1 = Label(self.frame_1, text='Cotação do Dólar Comercial', bg = '#dfe3ee',fg='#000000', font=('Calibri', 18, 'bold'))
        self.labelDolar1.place(relx=0.02, rely=0.12)

        self.labelDolar2 = Label(self.frame_1, text=dolar, bg = '#dfe3ee',fg='#000000', font=('Calibri', 16, 'bold'))
        self.labelDolar2.place(relx=0.02, rely=0.17)

        self.labelDolar2 = Label(self.frame_1, text=data, bg = '#dfe3ee',fg='#000000', font=('Calibri', 16, 'bold'))
        self.labelDolar2.place(relx=0.02, rely=0.22)

        self.labelcvuss = Label(self.frame_1, text='Digite o valor a ser convertido:', bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.labelcvuss.place(relx=0.02, rely=0.32)

        self.labelcvuss_entry = Entry(self.frame_1, font=('calibri', 14, 'bold'))
        self.labelcvuss_entry.place(relx=0.02, rely=0.37, relwidth=0.96, relheight=0.05)

        self.botaocvuss = Button(self.frame_1, text='Converter US$ em R$',border=2,bg='#109db2', fg='white', font=('verdana', 12, 'bold'), command= self.converte_USS_em_RS)
        self.botaocvuss.place(relx=0.02, rely=0.44, relwidth=0.96, relheight=0.10)

        self.botaocvuss = Button(self.frame_1, text='Converter US$ em R$',border=2,bg='#109db2', fg='white', font=('verdana', 12, 'bold'), command= self.converte_RS_em_USS)
        self.botaocvuss.place(relx=0.02, rely=0.56, relwidth=0.96, relheight=0.10)

    def converte_USS_em_RS(self):
        entrada_string = str(self.labelcvuss_entry.get()).replace(',','.')
        entrada = float(entrada_string)
        valor_dolar = float(self.Valor_dolar)
        final = round((entrada * valor_dolar),2)
        conversao = str(final).replace('.',',')
        self.labelconvertido = Label(self.frame_1, text='R$ ' + conversao, bg = '#dfe3ee',fg='#109db2', font=('Calibri', 18, 'bold'))
        self.labelconvertido.place(relx=0.02, rely=0.68, relwidth=0.96)

    def converte_RS_em_USS(self):
        entrada_string = str(self.labelcvuss_entry.get()).replace(',','.')
        entrada = float(entrada_string)
        valor_dolar = float(self.Valor_dolar)
        final = round((entrada / valor_dolar),2)
        conversao = str(final).replace('.',',')
        self.labelconvertido = Label(self.frame_1, text='US$ ' + conversao, bg = '#dfe3ee',fg='#109db2', font=('Calibri', 18, 'bold'))
        self.labelconvertido.place(relx=0.02, rely=0.68, relwidth=0.96)

    def cotaEuro(self):
        import requests
        import json
        requisicao = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')
        cotacao = requisicao.json()

        data = ('Data e Hora da Cotação:\n ' + cotacao['EUR']['create_date'])

        self.Valor_euro = round(float(cotacao['EUR']['bid']),2)

        valoreuro = str(self.Valor_euro).replace(".", ",")

        euro = ('Valor atual: R$ ' + valoreuro)

        self.labelEuro = Label(self.frame_2, text='Cotação do Euro Comercial', bg = '#dfe3ee',fg='#000000', font=('Calibri', 18, 'bold'))
        self.labelEuro.place(relx=0.02, rely=0.12)

        self.labelEuro2 = Label(self.frame_2, text=euro, bg = '#dfe3ee',fg='#000000', font=('Calibri', 16, 'bold'))
        self.labelEuro2.place(relx=0.02, rely=0.17)

        self.labelEuro3 = Label(self.frame_2, text=data, bg = '#dfe3ee',fg='#000000', font=('Calibri', 16, 'bold'))
        self.labelEuro3.place(relx=0.02, rely=0.22)

        self.labelcveuro = Label(self.frame_2, text='Digite o valor a ser convertido:', bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.labelcveuro.place(relx=0.02, rely=0.32)

        self.labelcveuro_entry = Entry(self.frame_2, font=('calibri', 14, 'bold'))
        self.labelcveuro_entry.place(relx=0.02, rely=0.37, relwidth=0.96, relheight=0.05)

        self.botaocveuro = Button(self.frame_2, text='Converter Euro em R$',border=2,bg='#109db2', fg='white', font=('verdana', 12, 'bold'), command= self.converte_Euro_em_RS)
        self.botaocveuro.place(relx=0.02, rely=0.44, relwidth=0.96, relheight=0.10)

        self.botaocveuro2 = Button(self.frame_2, text='Converter R$ em Euro',border=2,bg='#109db2', fg='white', font=('verdana', 12, 'bold'), command= self.converte_RS_em_Euro)
        self.botaocveuro2.place(relx=0.02, rely=0.56, relwidth=0.96, relheight=0.10)

    def converte_Euro_em_RS(self):
        entrada_string = str(self.labelcveuro_entry.get()).replace(',','.')
        entrada = float(entrada_string)
        valor_euro = float(self.Valor_euro)
        final = round((entrada * valor_euro),2)
        conversao = str(final).replace('.',',')
        self.labelconvertido = Label(self.frame_2, text='R$ ' + conversao, bg = '#dfe3ee',fg='#109db2', font=('Calibri', 18, 'bold'))
        self.labelconvertido.place(relx=0.02, rely=0.68, relwidth=0.96)

    def converte_RS_em_Euro(self):
        entrada_string = str(self.labelcveuro_entry.get()).replace(',','.')
        entrada = float(entrada_string)
        valor_euro = float(self.Valor_euro)
        final = round((entrada / valor_euro),2)
        conversao = str(final).replace('.',',')
        self.labelconvertido = Label(self.frame_2, text='€ ' + conversao, bg = '#dfe3ee',fg='#109db2', font=('Calibri', 18, 'bold'))
        self.labelconvertido.place(relx=0.02, rely=0.68, relwidth=0.96)

    def cotaBTC(self):
        import requests
        import json
        requisicao = requests.get('https://economia.awesomeapi.com.br/all/BTC-BRL')
        cotacao = requisicao.json()
        
        data = ('Data e Hora da Cotação:\n ' + cotacao['BTC']['create_date'])

        valorbtc = str(cotacao['BTC']['bid']).replace(".","")

        self.Valor_btc = float(valorbtc)

        bitcoin = str(cotacao['BTC']['bid'])+',00'

        btc = ('Valor atual: R$ ' + bitcoin)

        self.labelBtc = Label(self.frame_3, text='Cotação do BitCoin', bg = '#dfe3ee',fg='#000000', font=('Calibri', 18, 'bold'))
        self.labelBtc.place(relx=0.02, rely=0.12)

        self.labelBtc2 = Label(self.frame_3, text=btc, bg = '#dfe3ee',fg='#000000', font=('Calibri', 16, 'bold'))
        self.labelBtc2.place(relx=0.02, rely=0.17)

        self.labelBtc3 = Label(self.frame_3, text=data, bg = '#dfe3ee',fg='#000000', font=('Calibri', 16, 'bold'))
        self.labelBtc3.place(relx=0.02, rely=0.22)

        self.labelcvbtc = Label(self.frame_3, text='Digite o valor a ser convertido:', bg = '#dfe3ee',fg='#109db2', font=('Calibri', 14, 'bold'))
        self.labelcvbtc.place(relx=0.02, rely=0.32)

        self.labelcvbtc_entry = Entry(self.frame_3, font=('calibri', 14, 'bold'))
        self.labelcvbtc_entry.place(relx=0.02, rely=0.37, relwidth=0.96, relheight=0.05)

        self.botaocvbtc = Button(self.frame_3, text='Converter BitCoin em R$',border=2,bg='#109db2', fg='white', font=('verdana', 12, 'bold'), command= self.converte_Btc_em_RS)
        self.botaocvbtc.place(relx=0.02, rely=0.44, relwidth=0.96, relheight=0.10)

        self.botaocvbtc2 = Button(self.frame_3, text='Converter R$ em BitCoin',border=2,bg='#109db2', fg='white', font=('verdana', 12, 'bold'), command= self.converte_RS_em_Btc)
        self.botaocvbtc2.place(relx=0.02, rely=0.56, relwidth=0.96, relheight=0.10)

    def converte_Btc_em_RS(self):
        entrada_string = str(self.labelcvbtc_entry.get()).replace(',','.')
        entrada = float(entrada_string)
        valor_btc = float(self.Valor_btc)
        final = round((entrada * valor_btc),2)
        conversao = str(final).replace('.',',')
        self.labelconvertido = Label(self.frame_3, text='R$ ' + conversao, bg = '#dfe3ee',fg='#109db2', font=('Calibri', 18, 'bold'))
        self.labelconvertido.place(relx=0.02, rely=0.68, relwidth=0.96)

    def converte_RS_em_Btc(self):
        entrada_string = str(self.labelcvbtc_entry.get()).replace(',','.')
        entrada = float(entrada_string)
        valor_btc= float(self.Valor_btc)
        final = round((entrada / valor_btc),2)
        conversao = str(final).replace('.',',')
        self.labelconvertido = Label(self.frame_3, text='₿ ' + conversao, bg = '#dfe3ee',fg='#109db2', font=('Calibri', 18, 'bold'))
        self.labelconvertido.place(relx=0.02, rely=0.68, relwidth=0.96)

    def voltarMenuCota(self):
        self.telaMoeda.destroy()

Moeda()