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

def create_sacola():
    op = e_op.get()
    quantidade = e_quantidade_sacola.get()
    cod_produto = e_cod_produto.get()
    cpf = e_cpf_produto.get()
    comando = f'INSERT INTO alterasacola (op,qtd,cod_prod,cpf) VALUES ("{op}",{quantidade},{cod_produto},"{cpf}")'
    cursor.execute(comando)
    conexao.commit()

def select_produto():
    comando = f'SELECT * FROM alterasacola'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)

def update_produto():
    op = e_op.get()
    quantidade = e_quantidade_sacola.get()
    cod_produto = e_cod_produto.get()
    cpf = e_cpf_produto.get()
    comando = f'UPDATE produto SET op = {op},qtd = "{quantidade}",cod_prod = {cod_produto},cpf = "{cpf}" WHERE cod_prod = "{cod_produto}"'
    cursor.execute(comando)
    conexao.commit()

def delete_produto():
    cod_produto = e_cod_produto.get()
    comando = f'DELETE FROM alterasacola WHERE cod_prod = "{cod_produto}"'
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


l_altera_sacola = Label(frame_baixo, text='Alterar a sacola', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_altera_sacola.place(x=20, y=20)

l_op = Label(frame_baixo, text='Op', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_op.place(x=20, y=60)
e_op = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_op.place(x=20, y=80)

l_quantidade_sacola = Label(frame_baixo, text='Quantidade na Sacola', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_quantidade_sacola.place(x=20, y=100)
e_quantidade_sacola = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_quantidade_sacola.place(x=20, y=120)

l_cod_produto = Label(frame_baixo, text='Codigo do Produto*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_cod_produto.place(x=20, y=140)
e_cod_produto = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cod_produto.place(x=20, y=160)

l_cpf_produto = Label(frame_baixo, text='CPF*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_cpf_produto.place(x=20, y=180)
e_cpf_produto = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cpf_produto.place(x=20, y=200)

b_sacola_inserir = Button(frame_baixo, text='Inserir Produto', width=14, anchor=NW, font='Ivy 7 bold', bg=cor2_verde,
                           fg=cor1_branca, relief='raised', overrelief='ridge')
b_sacola_inserir.place(x=20, y=220)

b_sacola_remover = Button(frame_baixo, text='Remover Produto', width=14, anchor=NW, font='Ivy 7 bold',
                           bg=cor7_vermelha, fg=cor1_branca, relief='raised', overrelief='ridge')
b_sacola_remover.place(x=120, y=220)

b_sacola_atualizar = Button(frame_baixo, text='Atualizar Produto', width=14, anchor=NW, font='Ivy 7 bold',
                             bg=cor6_azul, fg=cor1_branca, relief='raised', overrelief='ridge')
b_sacola_atualizar.place(x=210, y=220)