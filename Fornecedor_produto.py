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


# CRUD

# Create

def create_fornecedor_produto():
    global e_cod_fornecedor_produto, e_data_fornecedor_produto
    global e_quantidade_fornecedor_produto, e_cnpj_fornecedor_produto
    cnpj = e_cnpj_fornecedor_produto.get()
    cod_prod = e_cod_fornecedor_produto.get()
    dataHora = e_data_fornecedor_produto.get()
    qtd = e_quantidade_fornecedor_produto.get()
    comando = f'INSERT INTO fornecedor_produto (cod_prod,dataHora,qtd) VALUES ({cod_prod},"{dataHora}",{qtd})'
    cursor.execute(comando)
    conexao.commit()


def select_fornecedor_produto():
    global e_cnpj_fornecedor_produto
    cnpj = e_cnpj_fornecedor_produto.get()
    comando = f'SELECT * FROM fornecedor_produto WHERE cnpj = "{cnpj}"'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)


def update_fornecedor_produto():
    global e_cod_fornecedor_produto, e_data_fornecedor_produto,e_cnpj_fornecedor_produto
    global e_quantidade_fornecedor_produto
    cod_prod = e_cod_fornecedor_produto.get()
    dataHora = e_data_fornecedor_produto.get()
    qtd = e_quantidade_fornecedor_produto.get()
    cnpj = e_cnpj_fornecedor_produto.get()
    comando = f'UPDATE fornecedor_produto SET cod_prod = {cod_prod},dataHora = "{dataHora}",qtd = "{qtd}" WHERE cnpj = "{cnpj}"'
    cursor.execute(comando)
    conexao.commit()


def delete_fornecedor_produto():
    global e_cnpj_fornecedor_produto
    cnpj = e_cnpj_fornecedor_produto.get()
    comando = f'DELETE FROM fornecedor_produto WHERE cnpj = {cnpj}'
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


l_produto = Label(frame_baixo, text='Origem do Produto', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_produto.place(x=20, y=20)

l_cod_fornecedor_produto = Label(frame_baixo, text='Codigo do Produto', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_cod_fornecedor_produto.place(x=20, y=60)
e_cod_fornecedor_produto = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cod_fornecedor_produto.place(x=20, y=80)

l_cnpj_fornecedor_produto = Label(frame_baixo, text='Cnpj do Fornecedor', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_cnpj_fornecedor_produto.place(x=20, y=100)
e_cnpj_fornecedor_produto = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cnpj_fornecedor_produto.place(x=20, y=120)

l_data_fornecedor_produto = Label(frame_baixo, text='Data de origem', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_data_fornecedor_produto.place(x=20, y=140)
e_data_fornecedor_produto = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_data_fornecedor_produto.place(x=20, y=160)

l_quantidade_fornecedor_produto = Label(frame_baixo, text='Quantidade', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_quantidade_fornecedor_produto.place(x=20, y=180)
e_quantidade_fornecedor_produto = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_quantidade_fornecedor_produto.place(x=20, y=200)

b_produto_inserir = Button(frame_baixo, text='Inserir Produto', command=create_fornecedor_produto,width=14, anchor=NW, font='Ivy 7 bold', bg=cor2_verde,
                          fg=cor1_branca, relief='raised', overrelief='ridge')
b_produto_inserir.place(x=20, y=220)

b_produto_remover = Button(frame_baixo, text='Remover Produto', command=delete_fornecedor_produto, width=16, anchor=NW, font='Ivy 7 bold',
                          bg=cor7_vermelha, fg=cor1_branca, relief='raised', overrelief='ridge')
b_produto_remover.place(x=120, y=220)

b_produto_atualizar = Button(frame_baixo, text='Atualizar Produto', command=update_fornecedor_produto, width=14, anchor=NW, font='Ivy 7 bold',
                            bg=cor6_azul, fg=cor1_branca, relief='raised', overrelief='ridge')
b_produto_atualizar.place(x=20, y=240)

b_produto_selecionar = Button(frame_baixo, text='Selecionar Produto', command=select_fornecedor_produto, width=16, anchor=NW, font='Ivy 7 bold',
                             bg=cor8_marrom, fg=cor1_branca, relief='raised', overrelief='ridge')
b_produto_selecionar.place(x=120, y=240)

janela.mainloop()
cursor.close()
conexao.close()