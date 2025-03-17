from tkinter import *

def botao_clicado():
    rotulo.config(text="Que legal! Vamos lá.")

def botao_clicado2():
    rotulo.config(text='Que pena! Feche o programa.')

# Criação da janela principal
janela = Tk()

# Define o título da janela
janela.title('POKEDEX')

# Define as dimensões da janela (largura x altura)
janela.geometry('500x500')

# Criação de RÓTULOS
rotulo = Label(janela, text='POKÉDEX', font=('Arial', 20), fg='red')
rotulo1 = Label(janela, text='Deseje procurar um Pokemon?', font=('Arial Bold', 18), fg='black', bg='red')

# Adiciona o rótulo à janela
rotulo.pack()
rotulo1.pack()

# Criação de botões

botao1 = Button(janela, text="Sim!", command=botao_clicado)
botao1.place(relx=0.45, rely=0.20, anchor=CENTER)

botao2 = Button(janela, text="Não!", command=botao_clicado2)
botao2.place(relx=0.55, rely=0.20, anchor=CENTER)

# Inicia o loop principal da aplicação
janela.mainloop()
