import mysql.connector
from tkinter import *
import os

# cores

cor0_preta = "#f0f3f5"
cor1_branca = "#feffff"
cor2_verde = "#4fa882"
cor3_valor = "#38576b"
cor4_letra = "#403d3d"
cor6_azul = "#038cfc"
cor7_vermelha = "#ef5350"
cor8_marrom = "#5C4033"

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Carlos12.',
    database='lojavirtual'
)

cursor = conexao.cursor()


def create_fornecedor():
    global e_CNPJ_fornecedor,e_nome_fornecedor
    cnpj = e_CNPJ_fornecedor.get()
    nome = e_nome_fornecedor.get()
    comando = f'INSERT INTO fornecedor (cnpj,nome) VALUES ("{cnpj}","{nome}")'
    cursor.execute(comando)
    conexao.commit()


def select_fornecedor():
    global e_CNPJ_fornecedor
    cnpj = e_CNPJ_fornecedor.get()
    comando = f'SELECT * FROM fornecedor WHERE cnpj = "{cnpj}"'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)


def update_fornecedor():
    global e_CNPJ_fornecedor, e_nome_fornecedor
    cnpj = e_CNPJ_fornecedor.get()
    nome = e_nome_fornecedor.get()
    comando = f'UPDATE fornecedor SET cnpj = "{cnpj}",nome = "{nome}" WHERE cnpj = "{cnpj}"'
    cursor.execute(comando)
    conexao.commit()

def delete_fornecedor():
    global e_CNPJ_fornecedor
    cnpj = e_CNPJ_fornecedor.get()
    comando = f'DELETE FROM fornecedor WHERE cnpj = "{cnpj}"'
    cursor.execute(comando)
    conexao.commit()

janela = Tk()

janela.title("Loja Virtual")

frame_cima = Frame(janela, width=300, height=50, bg=cor2_verde, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=300, height=300, bg=cor1_branca, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

app_nome = Label(frame_cima, text='Loja Virtual', anchor=NW, font='Ivy 13 bold', bg=cor2_verde, fg=cor1_branca,
                 relief='flat')
app_nome.place(x=90, y=20)


l_fornecedor = Label(frame_baixo, text='Fornecedor', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                     relief='flat')
l_fornecedor.place(x=50, y=20)

l_CNPJ_fornecedor = Label(frame_baixo, text='CNPJ', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                          relief='flat')
l_CNPJ_fornecedor.place(x=50, y=40)
e_CNPJ_fornecedor = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_CNPJ_fornecedor.place(x=50, y=60)

l_nome_fornecedor = Label(frame_baixo, text='Nome do Fornecedor', anchor=NW, font='Ivy 13 bold', bg=cor1_branca,
                          fg=cor4_letra,
                          relief='flat')
l_nome_fornecedor.place(x=50, y=80)
e_nome_fornecedor = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_nome_fornecedor.place(x=50, y=100)


b_produto_inserir = Button(frame_baixo, text='Inserir Fornecedor', command=create_fornecedor, width=14, anchor=NW, font='Ivy 7 bold', bg=cor2_verde, fg=cor1_branca, relief='raised', overrelief='ridge')
b_produto_inserir.place(x=20, y=120)

b_produto_remover = Button(frame_baixo, text='Remover Fornecedor', command=delete_fornecedor, width=16, anchor=NW, font='Ivy 7 bold', bg=cor7_vermelha, fg=cor1_branca, relief='raised', overrelief='ridge')
b_produto_remover.place(x=120, y=120)

b_produto_atualizar = Button(frame_baixo, text='Atualizar Fornecedor', command=update_fornecedor, width=14, anchor=NW, font='Ivy 7 bold', bg=cor6_azul, fg=cor1_branca, relief='raised', overrelief='ridge')
b_produto_atualizar.place(x=20, y=140)

b_produto_selecionar = Button(frame_baixo, text='Selecionar Fornecedor', command=select_fornecedor, width=16, anchor=NW, font='Ivy 7 bold', bg=cor8_marrom, fg=cor1_branca, relief='raised', overrelief='ridge')
b_produto_selecionar.place(x=120, y=140)


janela.mainloop()
cursor.close()
conexao.close()
