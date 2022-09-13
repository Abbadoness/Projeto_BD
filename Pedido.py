from tkinter import *

import Persistencia

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


global e_data_pedido, e_numero_pedido, e_gasto, e_cep, e_estado, e_cidade, e_cod_endereco, e_complemento, e_cartao_credito, e_cartao_vencimento, e_cartao_cvv, e_cod_ped

janela = Tk()

janela.title("Loja Virtual")

frame_cima = Frame(janela, width=800, height=50, bg=cor2_verde, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=800, height=600, bg=cor1_branca, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

app_nome = Label(frame_cima, text='Loja Virtual', anchor=NW, font='Ivy 13 bold', bg=cor2_verde, fg=cor1_branca,
                 relief='flat')
app_nome.place(x=90, y=20)

l_pedido = Label(frame_baixo, text='Pedido', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                 relief='flat')
l_pedido.place(x=20, y=20)

l_cod_ped = Label(frame_baixo, text='Codigo do Pedido', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                  relief='flat')
l_cod_ped.place(x=20, y=60)
e_cod_ped = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cod_ped.place(x=20, y=80)

l_data_pedido = Label(frame_baixo, text='Data do Pedido', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                      relief='flat')
l_data_pedido.place(x=20, y=100)
e_data_pedido = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_data_pedido.place(x=20, y=120)

l_gasto = Label(frame_baixo, text='Gasto', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_gasto.place(x=20, y=140)
e_gasto = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_gasto.place(x=20, y=160)

l_numero_pedido = Label(frame_baixo, text='Numero Pedido', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                        relief='flat')
l_numero_pedido.place(x=20, y=180)
e_numero_pedido = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_numero_pedido.place(x=20, y=200)

b_pedido_inserir = Button(frame_baixo, text='Inserir Pedido', command=Persistencia.create_pedido, width=14,
                          anchor=NW,
                          font='Ivy 7 bold', bg=cor2_verde,
                          fg=cor1_branca, relief='raised', overrelief='ridge')
b_pedido_inserir.place(x=20, y=220)

b_pedido_remover = Button(frame_baixo, text='Remover Pedido', command=delete_pedido, width=14, anchor=NW,
                          font='Ivy 7 bold',
                          bg=cor7_vermelha, fg=cor1_branca, relief='raised', overrelief='ridge')
b_pedido_remover.place(x=120, y=220)

b_pedido_atualizar = Button(frame_baixo, text='Atualizar Pedido', command=update_pedido, width=14, anchor=NW,
                            font='Ivy 7 bold',
                            bg=cor6_azul, fg=cor1_branca, relief='raised', overrelief='ridge')
b_pedido_atualizar.place(x=20, y=240)

b_pedido_selecionar = Button(frame_baixo, text='Selecionar Pedido', command=select_pedido, width=14, anchor=NW,
                             font='Ivy 7 bold',
                             bg=cor8_marrom, fg=cor1_branca, relief='raised', overrelief='ridge')
b_pedido_selecionar.place(x=120, y=240)

l_endereco = Label(frame_baixo, text='Endereco*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                   relief='flat')
l_endereco.place(x=500, y=20)

l_cidade = Label(frame_baixo, text='Cidade*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                 relief='flat')
l_cidade.place(x=500, y=60)
e_cidade = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cidade.place(x=500, y=85)

l_estado = Label(frame_baixo, text='Estado*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                 relief='flat')
l_estado.place(x=500, y=105)
e_estado = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_estado.place(x=500, y=125)

l_cep = Label(frame_baixo, text='CEP*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra, relief='flat')
l_cep.place(x=500, y=145)
e_cep = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cep.place(x=500, y=165)

l_complemento = Label(frame_baixo, text='Complemento', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                      relief='flat')
l_complemento.place(x=500, y=185)
e_complemento = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_complemento.place(x=500, y=205)

l_cod_endereco = Label(frame_baixo, text='Codigo do Endereco', anchor=NW, font='Ivy 13 bold', bg=cor1_branca,
                       fg=cor4_letra, relief='flat')
l_cod_endereco.place(x=500, y=225)
e_cod_endereco = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cod_endereco.place(x=500, y=245)

b_endereco_inserir = Button(frame_baixo, text='Inserir Endereco', command=create_endereco, width=14, anchor=NW,
                            font='Ivy 7 bold', bg=cor2_verde, fg=cor1_branca, relief='raised', overrelief='ridge')
b_endereco_inserir.place(x=500, y=265)

b_endereco_remover = Button(frame_baixo, text='Remover Endereco', command=delete_endereco, width=16, anchor=NW,
                            font='Ivy 7 bold', bg=cor7_vermelha, fg=cor1_branca, relief='raised', overrelief='ridge')
b_endereco_remover.place(x=600, y=265)

b_endereco_atualizar = Button(frame_baixo, text='Atualizar Endereco', command=update_endereco, width=14, anchor=NW,
                              font='Ivy 7 bold', bg=cor6_azul, fg=cor1_branca, relief='raised', overrelief='ridge')
b_endereco_atualizar.place(x=500, y=285)

b_endereco_selecionar = Button(frame_baixo, text='Selecionar Endereco', command=select_endereco, width=16,
                               anchor=NW, font='Ivy 7 bold', bg=cor8_marrom, fg=cor1_branca, relief='raised',
                               overrelief='ridge')
b_endereco_selecionar.place(x=600, y=285)

# Cartão

l_cartao = Label(frame_baixo, text='Cartao de credito', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                 relief='flat')
l_cartao.place(x=10, y=340)

l_cartao_credito = Label(frame_baixo, text='Numero do cartao*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca,
                         fg=cor4_letra, relief='flat')
l_cartao_credito.place(x=10, y=360 + 20)
e_cartao_credito = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cartao_credito.place(x=13, y=380 + 20)

l_cartao_cvv = Label(frame_baixo, text='CVV*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca, fg=cor4_letra,
                     relief='flat')
l_cartao_cvv.place(x=10, y=400 + 20)
e_cartao_cvv = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cartao_cvv.place(x=13, y=420 + 20)

l_cartao_vencimento = Label(frame_baixo, text='Vencimento*', anchor=NW, font='Ivy 13 bold', bg=cor1_branca,
                            fg=cor4_letra, relief='flat')
l_cartao_vencimento.place(x=10, y=440 + 20)
e_cartao_vencimento = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cartao_vencimento.place(x=13, y=460 + 20)

b_cartao_inserir = Button(frame_baixo, text='Inserir Cartao', command=create_cartao, width=14, anchor=NW,
                          font='Ivy 7 bold', bg=cor2_verde, fg=cor1_branca, relief='raised', overrelief='ridge')
b_cartao_inserir.place(x=13, y=480 + 20)

b_cartao_remover = Button(frame_baixo, text='Remover Cartao', command=delete_cartao, width=16, anchor=NW,
                          font='Ivy 7 bold', bg=cor7_vermelha, fg=cor1_branca, relief='raised', overrelief='ridge')
b_cartao_remover.place(x=120, y=480 + 20)

b_cartao_atualizar = Button(frame_baixo, text='Atualizar Cartao', command=update_cartao, width=14, anchor=NW,
                            font='Ivy 7 bold', bg=cor6_azul, fg=cor1_branca, relief='raised', overrelief='ridge')
b_cartao_atualizar.place(x=13, y=500 + 20)

b_cartao_selecionar = Button(frame_baixo, text='Selecionar Cartao', command=select_cartao, width=16, anchor=NW,
                             font='Ivy 7 bold', bg=cor8_marrom, fg=cor1_branca, relief='raised', overrelief='ridge')
b_cartao_selecionar.place(x=120, y=500 + 20)

janela.mainloop()
cursor.close()
conexao.close()
