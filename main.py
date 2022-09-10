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


pastaApp = os.path.dirname(__file__)


def menuCliente():
    exec(open(pastaApp + "\\Cliente.py").read())


def menuFornecedor():
    exec(open(pastaApp + "\\Fornecedor.py").read())


def menuProduto():
    exec(open(pastaApp + "\\Produto.py").read())

def menuAlteraSacola():
    exec(open(pastaApp + "\\AlteraSacola.py").read())

janela = Tk()

janela.title("Loja Virtual")

barraDeMenus = Menu(janela)
menuBanco = Menu(barraDeMenus, tearoff=0)
menuBanco.add_command(label="Cliente", command=menuCliente)
menuBanco.add_command(label="Pedido")
menuBanco.add_command(label="Altera Sacola", command=menuAlteraSacola)
menuBanco.add_command(label="Produto", command=menuProduto)
menuBanco.add_command(label="Fornecedor", command=menuFornecedor)
menuBanco.add_separator()
menuBanco.add_command(label="Sair", command=janela.quit)
barraDeMenus.add_cascade(label="Entidades", menu=menuBanco)
janela.config(menu=barraDeMenus)

frame_cima = Frame(janela, width=1300, height=50, bg=cor2_verde, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=1300, height=718, bg=cor1_branca, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

app_nome = Label(frame_cima, text='Loja Virtual', anchor=NW, font='Ivy 13 bold', bg=cor2_verde, fg=cor1_branca,
                 relief='flat')
app_nome.place(x=350, y=20)

# Frame baixo


# Produto


l_pedido = Label(frame_baixo, text='Pedido', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_pedido.place(x=450, y=20)

l_cod_ped = Label(frame_baixo, text='Codigo do Pedido', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_cod_ped.place(x=450, y=60)
e_cod_ped = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cod_ped.place(x=450, y=80)

l_data_pedido = Label(frame_baixo, text='Data do Pedido', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_data_pedido.place(x=450, y=100)
e_data_pedido = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_data_pedido.place(x=450, y=120)

l_gasto = Label(frame_baixo, text='Gasto', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_gasto.place(x=450, y=140)
e_gasto = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_gasto.place(x=450, y=160)


b_pedido_inserir = Button(frame_baixo, text='Inserir Pedido', width=14, anchor=NW, font='Ivy 7 bold', bg=cor2_verde,
                           fg=cor1_branca, relief='raised', overrelief='ridge')
b_pedido_inserir.place(x=450, y=180)

b_pedido_remover = Button(frame_baixo, text='Remover Pedido', width=14, anchor=NW, font='Ivy 7 bold',
                           bg=cor7_vermelha, fg=cor1_branca, relief='raised', overrelief='ridge')
b_pedido_remover.place(x=550, y=180)

b_pedido_atualizar = Button(frame_baixo, text='Atualizar Pedido', width=14, anchor=NW, font='Ivy 7 bold',
                             bg=cor6_azul, fg=cor1_branca, relief='raised', overrelief='ridge')
b_pedido_atualizar.place(x=650, y=180)

b_pedido_selecionar = Button(frame_baixo, text='Selecionar Pedido', width=14, anchor=NW, font='Ivy 7 bold',
                             bg=cor6_azul, fg=cor1_branca, relief='raised', overrelief='ridge')
b_pedido_selecionar.place(x=750, y=180)


# CRUD

# Create
'''def create_cliente():
    cpf = e_cpf.get()
    nome = e_nome.get()
    dataNasc = e_data_nascimento.get()
    comando = f'INSERT INTO cliente (cpf,nome,dataNasc) VALUES ("{cpf}","{nome}",{dataNasc})'
    cursor.execute(comando)
    conexao.commit()'''

# Read

'''comando = f'SELECT * FROM carrinho'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)'''

# Update
'''cod_car = 6
total = 200
comando = f'UPDATE carrinho SET total = {total} WHERE cod_car = {cod_car}'
cursor.execute(comando)
conexao.commit()'''

# Delete

'''cod_car = 6
comando = f'DELETE FROM carrinho WHERE cod_car = {cod_car}'
cursor.execute(comando)
conexao.commit()'''

janela.mainloop()
cursor.close()
conexao.close()
