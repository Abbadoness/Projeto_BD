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

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Carlos12.',
    database='lojavirtual'
)

cursor = conexao.cursor()


# CRUD

# Create

def create_produto():
    nome = e_nome_produto.get()
    preco = e_preco_produto.get()
    comando = f'INSERT INTO produto (nome,preco) VALUES ("{nome}",{preco})'
    cursor.execute(comando)
    conexao.commit()


def select_produto():
    comando = f'SELECT * FROM produto'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)


def update_produto():
    preco = e_preco_produto.get()
    nome = e_nome_produto.get()
    estoque = e_estoque_produto.get()
    comando = f'UPDATE produto SET preco = {preco},nome = "{nome}",estoque = {estoque} WHERE nome = "{nome}"'
    cursor.execute(comando)
    conexao.commit()


def delete_produto():
    nome = e_nome_produto.get()
    comando = f'DELETE FROM produto WHERE nome = "{nome}"'
    cursor.execute(comando)
    conexao.commit()


janela = Tk()

janela.title("Loja Virtual")

frame_cima = Frame(janela, width=1300, height=50, bg=cor2_verde, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=1300, height=718, bg=cor1_branca, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

app_nome = Label(frame_cima, text='Loja Virtual', anchor=NW, font='Ivy 13 bold', bg=cor2_verde, fg=cor1_branca,
                 relief='flat')
app_nome.place(x=350, y=20)


l_produto = Label(frame_baixo, text='Produto', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_produto.place(x=20, y=20)

l_nome_produto = Label(frame_baixo, text='Nome do produto', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_nome_produto.place(x=20, y=60)
e_nome_produto = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_nome_produto.place(x=20, y=80)

l_preco_produto = Label(frame_baixo, text='Preco do produto', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_preco_produto.place(x=20, y=100)
e_preco_produto = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_preco_produto.place(x=20, y=120)

l_estoque_produto = Label(frame_baixo, text='Estoque*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_estoque_produto.place(x=20, y=140)
e_estoque_produto = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_estoque_produto.place(x=20, y=160)

b_produto_inserir = Button(frame_baixo, text='Inserir Produto', width=14, anchor=NW, font='Ivy 7 bold', bg=cor2_verde,
                           fg=cor1_branca, relief='raised', overrelief='ridge')
b_produto_inserir.place(x=23, y=180)

b_produto_remover = Button(frame_baixo, text='Remover Produto', width=14, anchor=NW, font='Ivy 7 bold',
                           bg=cor7_vermelha, fg=cor1_branca, relief='raised', overrelief='ridge')
b_produto_remover.place(x=120, y=180)

b_produto_atualizar = Button(frame_baixo, text='Atualizar Produto', width=14, anchor=NW, font='Ivy 7 bold',
                             bg=cor6_azul, fg=cor1_branca, relief='raised', overrelief='ridge')
b_produto_atualizar.place(x=220, y=180)

janela.mainloop()
cursor.close()
conexao.close()