from imports import *

class Relatorios():
    def printCliente(self):
        webbrowser.open('cliente.pdf') #Abre o browser e cria o arquivo PDF
    
    def geraRelatorio(self):
        self.pdfCliente = canvas.Canvas('cliente.pdf') # Variavel do PDF

    

    # Variaveis Do Entry para sair no PDF
        self.codigoRelat = self.entry_codigo.get()
        self.nomeRelat = self.entry_nome.get()
        self.telefoneRelat = self.entry_telefone.get()
        self.cidadeRelat = self.entry_cidade.get()

        self.pdfCliente.setFont('Helvetica-Bold', 24) # Fonte do relatorio
        self.pdfCliente.drawString(200, 790, 'Ficha do Cliente') # Titulo do Relatório

        # Campos em negrito
        self.pdfCliente.setFont('Helvetica-Bold', 18) 
        self.pdfCliente.drawString(50, 700, 'Código: ')
        self.pdfCliente.drawString(50, 670, 'Nome: ')
        self.pdfCliente.drawString(50, 640, 'Telefone: ')
        self.pdfCliente.drawString(50, 610, 'Cidade: ')

        self.pdfCliente.setFont('Helvetica', 18) 
        self.pdfCliente.drawString(123, 700, self.codigoRelat)
        self.pdfCliente.drawString(110, 670, self.nomeRelat)
        self.pdfCliente.drawString(132, 640, self.telefoneRelat)
        self.pdfCliente.drawString(120, 610,  self.cidadeRelat)

        self.pdfCliente.showPage()
        self.pdfCliente.save()
        self.printCliente()