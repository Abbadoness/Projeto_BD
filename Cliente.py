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
    cpf = e_cpf.get()
    nome = e_nome.get()
    dataNasc = e_data_nascimento.get()
    comando = f'INSERT INTO cliente (cpf,nome,dataNasc) VALUES ("{cpf}","{nome}","{dataNasc}")'
    cursor.execute(comando)
    conexao.commit()


def create_endereco():
    cep = e_cep.get()
    estado = e_estado.get()
    cidade = e_cidade.get()
    comando = f'INSERT INTO endereco (cep,estado,cidade) VALUES ("{cep}","{estado}","{cidade}")'
    cursor.execute(comando)
    conexao.commit()


def create_cartao():
    numero = e_cartao_credito.get()
    vencimento = e_cartao_vencimento.get()
    cvv = e_cartao_cvv.get()
    comando = f'INSERT INTO cartao (numero,vencimento,cvv) VALUES ("{numero}","{vencimento}","{cvv}")'
    cursor.execute(comando)
    conexao.commit()


# Read
def select_cliente():
    comando = f'SELECT * FROM cliente'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)


def select_endereco():
    comando = f'SELECT * FROM endereco'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)


def select_cartao():
    comando = f'SELECT * FROM cartao'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)


# Update

def update_cliente():
    cpf = e_cpf.get()
    nome = e_nome.get()
    dataNasc = e_data_nascimento.get()
    comando = f'UPDATE cliente SET cpf = {cpf},nome = "{nome}",dataNasc = "{dataNasc}" WHERE cpf = {cpf}'
    cursor.execute(comando)
    conexao.commit()


def update_endereco():
    cidade = e_cidade.get()
    estado = e_estado.get()
    cep = e_cep.get()
    comando = f'UPDATE endereco SET cep = "{cep}",estado = "{estado}",cidade = "{cidade}"'
    cursor.execute(comando)
    conexao.commit()


def update_cartao():
    numero = e_cartao_credito.get()
    cvv = e_cartao_cvv.get()
    vencimento = e_cartao_vencimento.get()
    comando = f'UPDATE cartao SET numero = "{numero}",cvv = "{cvv}",vencimento = {vencimento} WHERE numero = "{numero}"'
    cursor.execute(comando)
    conexao.commit()


# Delete

def delete_cliente():
    cpf = e_cpf.get()
    comando = f'DELETE FROM cliente WHERE cpf = {cpf}'
    cursor.execute(comando)
    conexao.commit()


def delete_endereco():
    cpf = e_cpf.get()
    comando = f'DELETE FROM cliente WHERE cpf = {cpf}'
    cursor.execute(comando)
    conexao.commit()


def delete_cartao():
    numero = e_cartao_credito.get()
    comando = f'DELETE FROM cartao WHERE numero = "{numero}"'
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

l_data_nascimento = Label(frame_baixo, text='Data de nascimento*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca,
                          fg=cor4_letra, relief='flat')
l_data_nascimento.place(x=10, y=140)
e_data_nascimento = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_data_nascimento.place(x=13, y=160)

l_sacola = Label(frame_baixo, text='Sacola*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca,
                          fg=cor4_letra, relief='flat')
l_sacola.place(x=10, y=180)
e_sacola = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_sacola.place(x=13, y=200)

b_cliente_inserir = Button(frame_baixo, command=create_cliente, text='Inserir Cliente', width=11, anchor=NW,
                           font='Ivy 7 bold', bg=cor2_verde,
                           fg=cor1_branca, relief='raised', overrelief='ridge')
b_cliente_inserir.place(x=13, y=220)

b_cliente_remover = Button(frame_baixo, command=delete_cliente, text='Remover Cliente', width=13, anchor=NW,
                           font='Ivy 7 bold',
                           bg=cor7_vermelha, fg=cor1_branca, relief='raised', overrelief='ridge')
b_cliente_remover.place(x=95, y=220)

b_cliente_atualizar = Button(frame_baixo, command=update_cliente, text='Atualizar Cliente', width=13, anchor=NW,
                             font='Ivy 7 bold',
                             bg=cor6_azul, fg=cor1_branca, relief='raised', overrelief='ridge')
b_cliente_atualizar.place(x=190, y=220)

# Endereço


l_endereco = Label(frame_baixo, text='Endereco*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                   relief='flat')
l_endereco.place(x=10, y=420)

l_cidade = Label(frame_baixo, text='Cidade*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                 relief='flat')
l_cidade.place(x=10, y=460)
e_cidade = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cidade.place(x=13, y=485)

l_estado = Label(frame_baixo, text='Estado*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                 relief='flat')
l_estado.place(x=10, y=505)
e_estado = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_estado.place(x=13, y=525)

l_cep = Label(frame_baixo, text='CEP*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_cep.place(x=10, y=545)
e_cep = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cep.place(x=13, y=565)

b_endereco_inserir = Button(frame_baixo, text='Inserir Endereco', width=14, anchor=NW, font='Ivy 7 bold', bg=cor2_verde,
                            fg=cor1_branca, relief='raised', overrelief='ridge')
b_endereco_inserir.place(x=13, y=585)

b_endereco_remover = Button(frame_baixo, text='Remover Endereco', width=14, anchor=NW, font='Ivy 7 bold',
                            bg=cor7_vermelha, fg=cor1_branca, relief='raised', overrelief='ridge')
b_endereco_remover.place(x=95, y=585)

b_endereco_atualizar = Button(frame_baixo, text='Atualizar Endereco', width=14, anchor=NW, font='Ivy 7 bold',
                              bg=cor6_azul, fg=cor1_branca, relief='raised', overrelief='ridge')
b_endereco_atualizar.place(x=190, y=585)

# Cartão

l_cartao = Label(frame_baixo, text='Cartao de credito', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                 relief='flat')
l_cartao.place(x=10, y=240)

l_cartao_credito = Label(frame_baixo, text='Numero do cartao*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca,
                         fg=cor4_letra, relief='flat')
l_cartao_credito.place(x=10, y=280)
e_cartao_credito = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cartao_credito.place(x=13, y=300)

l_cartao_cvv = Label(frame_baixo, text='CVV*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                     relief='flat')
l_cartao_cvv.place(x=10, y=320)
e_cartao_cvv = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cartao_cvv.place(x=13, y=340)

l_cartao_vencimento = Label(frame_baixo, text='Vencimento*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca,
                            fg=cor4_letra, relief='flat')
l_cartao_vencimento.place(x=10, y=360)
e_cartao_vencimento = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cartao_vencimento.place(x=13, y=380)

b_cartao_inserir = Button(frame_baixo, text='Inserir Cartao', width=11, anchor=NW, font='Ivy 7 bold', bg=cor2_verde,
                          fg=cor1_branca, relief='raised', overrelief='ridge')
b_cartao_inserir.place(x=13, y=400)

b_cartao_remover = Button(frame_baixo, text='Remover Cartao', width=13, anchor=NW, font='Ivy 7 bold', bg=cor7_vermelha,
                          fg=cor1_branca, relief='raised', overrelief='ridge')
b_cartao_remover.place(x=95, y=400)

b_cartao_atualizar = Button(frame_baixo, text='Atualizar Cartao', width=13, anchor=NW, font='Ivy 7 bold', bg=cor6_azul,
                            fg=cor1_branca, relief='raised', overrelief='ridge')
b_cartao_atualizar.place(x=190, y=400)

janela.mainloop()
cursor.close()
conexao.close()
