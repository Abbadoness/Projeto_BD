# -- coding: UTF-8 --

import mysql.connector
from tkinter import *


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
def create_cliente():
    global e_sacola,e_data_nascimento,e_nome,e_cpf
    cpf = e_cpf.get()
    nome = e_nome.get()
    dataNasc = e_data_nascimento.get()
    sacola = e_sacola.get()
    comando = f'INSERT INTO cliente (cpf,nome,dataNasc,sacola) VALUES ("{cpf}","{nome}","{dataNasc}",{sacola})'
    cursor.execute(comando)
    conexao.commit()


# Read
def select_cliente():
    global e_cpf
    cpf = e_cpf.get()
    comando = f'SELECT * FROM cliente WHERE cpf = "{cpf}"'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)


# Update

def update_cliente():
    global e_sacola,e_cpf,e_nome,e_data_nascimento
    sacola = e_sacola.get()
    cpf = e_cpf.get()
    nome = e_nome.get()
    dataNasc = e_data_nascimento.get()
    comando = f'UPDATE cliente SET cpf = "{cpf}",nome = "{nome}",dataNasc = "{dataNasc}",sacola ={sacola}  WHERE cpf = "{cpf}"'
    cursor.execute(comando)
    conexao.commit()


# Delete

def delete_cliente():
    global e_cpf
    cpf = e_cpf.get()
    comando = f'DELETE FROM cliente WHERE cpf = "{cpf}"'
    cursor.execute(comando)
    conexao.commit()


janela = Tk()
janela.title("Loja Virtual")

frame_cima = Frame(janela, width=800, height=50, bg=cor2_verde, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=800, height=500, bg=cor1_branca, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

app_nome = Label(frame_cima, text='Loja Virtual', anchor=NW, font='Ivy 13 bold', bg=cor2_verde, fg=cor1_branca,
                 relief='flat')
app_nome.place(x=350, y=20)

# Frame baixo

l_cliente = Label(frame_baixo, text='Cliente', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                  relief='flat')
l_cliente.place(x=10, y=20)

l_nome = Label(frame_baixo, text='Nome*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_nome.place(x=10, y=60)
e_nome = Entry(frame_baixo, width=50, justify='left', relief='solid')
e_nome.place(x=13, y=80)

l_cpf = Label(frame_baixo, text='CPF*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_cpf.place(x=10, y=100)
e_cpf = Entry(frame_baixo, width=50, justify='left', relief='solid')
e_cpf.place(x=13, y=120)

l_data_nascimento = Label(frame_baixo, text='Data de nascimento', anchor=NW, font='Ivy 13 bold', bg=cor1_branca,
                          fg=cor4_letra, relief='flat')
l_data_nascimento.place(x=10, y=140)
e_data_nascimento = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_data_nascimento.place(x=13, y=160)

l_sacola = Label(frame_baixo, text='Sacola', anchor=NW, font='Ivy 13 bold', bg=cor1_branca,
                          fg=cor4_letra, relief='flat')
l_sacola.place(x=10, y=180)
e_sacola = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_sacola.place(x=13, y=200)

b_cliente_inserir = Button(frame_baixo, text='Inserir Cliente', command=create_cliente, width=14, anchor=NW, font='Ivy 7 bold', bg=cor2_verde, fg=cor1_branca, relief='raised', overrelief='ridge')
b_cliente_inserir.place(x=13, y=220)

b_cliente_remover = Button(frame_baixo, text='Remover Cliente', command=delete_cliente, width=16, anchor=NW, font='Ivy 7 bold', bg=cor7_vermelha, fg=cor1_branca, relief='raised', overrelief='ridge')
b_cliente_remover.place(x=120, y=220)

b_cliente_atualizar = Button(frame_baixo, text='Atualizar Cliente', command=update_cliente, width=14, anchor=NW, font='Ivy 7 bold', bg=cor6_azul, fg=cor1_branca, relief='raised', overrelief='ridge')
b_cliente_atualizar.place(x=13, y=240)

b_cliente_selecionar = Button(frame_baixo, text='Selecionar Cliente', command=select_cliente, width=16, anchor=NW, font='Ivy 7 bold', bg=cor8_marrom, fg=cor1_branca, relief='raised', overrelief='ridge')
b_cliente_selecionar.place(x=120, y=240)


janela.mainloop()
cursor.close()
conexao.close()
