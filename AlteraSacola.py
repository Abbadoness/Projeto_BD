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

def create_sacola():
    global e_op,e_quantidade_sacola,e_cod_produto,e_cpf_produto
    op = e_op.get()
    quantidade = e_quantidade_sacola.get()
    cod_produto = e_cod_produto.get()
    cpf = e_cpf_produto.get()
    comando = f'INSERT INTO alterasacola (cod_prod, op, qtd) VALUES ({cod_produto},"{op}",{quantidade})'
    cursor.execute(comando)
    conexao.commit()

def select_produto():
    global e_cod_op_produto
    cod_op = e_cod_op_produto.get()
    comando = f'SELECT * FROM alterasacola WHERE cod_op = {cod_op}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)

def update_produto():
    global e_op, e_quantidade_sacola, e_cod_produto, e_cpf_produto, e_cod_op_produto
    op = e_op.get()
    cod_op = e_cod_op_produto.get()
    quantidade = e_quantidade_sacola.get()
    cod_produto = e_cod_produto.get()
    cpf = e_cpf_produto.get()
    comando = f'UPDATE alterasacola SET op = "{op}",qtd = "{quantidade}",cod_prod = {cod_produto} WHERE cod_op = {cod_op}'
    cursor.execute(comando)
    conexao.commit()

def delete_produto():
    global e_cod_op_produto
    cod_op = e_cod_op_produto.get()
    comando = f'DELETE FROM alterasacola WHERE cod_op = {cod_op}'
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

l_cod_op_produto = Label(frame_baixo, text='Codigo op', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_cod_op_produto.place(x=20, y=220)
e_cod_op_produto = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cod_op_produto.place(x=20, y=240)


b_alteraSacola_inserir = Button(frame_baixo, text='Inserir na Sacola', command=create_sacola, width=14, anchor=NW, font='Ivy 7 bold', bg=cor2_verde,
                          fg=cor1_branca, relief='raised', overrelief='ridge')
b_alteraSacola_inserir.place(x=20, y=220+40)

b_alteraSacola_remover = Button(frame_baixo, text='Remover da Sacola', command=delete_produto, width=16, anchor=NW, font='Ivy 7 bold',
                          bg=cor7_vermelha, fg=cor1_branca, relief='raised', overrelief='ridge')
b_alteraSacola_remover.place(x=120, y=220+40)

b_alteraSacola_atualizar = Button(frame_baixo, text='Atualizar a Sacola', command=update_produto, width=14, anchor=NW, font='Ivy 7 bold',
                            bg=cor6_azul, fg=cor1_branca, relief='raised', overrelief='ridge')
b_alteraSacola_atualizar.place(x=20, y=240+40)

b_alteraSacola_selecionar = Button(frame_baixo, text='Selecionar da Sacola', command=select_produto, width=16, anchor=NW, font='Ivy 7 bold',
                             bg=cor8_marrom, fg=cor1_branca, relief='raised', overrelief='ridge')
b_alteraSacola_selecionar.place(x=120, y=240+40)

janela.mainloop()
cursor.close()
conexao.close()
