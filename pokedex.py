from tkinter import *
from tkinter import ttk

def selecionar_opcao(event):
    # Obtém a opção selecionada na Combobox
    opcao_selecionada = caixinha.get()
    resultado.config(text=f"Opção selecionada: {opcao_selecionada}")

def exibir_entrada():
    texto = campo_entrada.get()
    resultado2.config(text=f'Texto inserido: {texto}')

# Criação da janela principal
janela = Tk()
janela.title('POKEDEX')
janela.geometry('500x500')

# Criando uma lista de opções para o Combobox
opcoes = ['Pikachu', 'Bulbasaur', 'Charmander', 'Gyarados', 'Gengar', 'Dragonite']

# Criação de RÓTULOS
rotulo = Label(janela, text='POKÉDEX', font=('MS Sans Serif', 30), fg='red')
rotulo.pack()
rotulo1 = Label(janela, text='Deseje procurar um Pokemon?', font=('Arial', 16), fg='black', bg='red')
rotulo1.pack()

# Criando a Combobox
caixinha = ttk.Combobox(janela, values=opcoes)
caixinha.pack(pady=10)
caixinha.set("Escolha uma opção")

# Adicionando um evento de seleção à Combobox
caixinha.bind("<<ComboboxSelected>>", selecionar_opcao)

resultado = Label(janela, text="")
resultado.pack(pady=10)

# Criação de botões

'''botao1 = Button(janela, text="Sim!", command=botao_clicado)
botao1.place(relx=0.45, rely=0.20, anchor=CENTER)

botao2 = Button(janela, text="Não!", command=botao_clicado2)
botao2.place(relx=0.55, rely=0.20, anchor=CENTER) '''

# Entrada de dados
campo_entrada = Entry(janela, width=30)
campo_entrada.pack(pady=10)

botao_exibir = Button(janela, text='Exibir Entrada', command=exibir_entrada)
botao_exibir.pack()

resultado2 = Label(janela, text='')
resultado2.pack(pady=10)

# Inicia o loop principal da aplicação
janela.mainloop()
