from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

'''def selecionar_opcao(event):
    # Obtém a opção selecionada na Combobox
    opcao_selecionada = caixinha.get()
    resultado.config(text=f"Opção selecionada: {opcao_selecionada}")

def exibir_entrada():
    texto = campo_entrada.get()
    resultado2.config(text=f'Texto inserido: {texto}')'''

# Letra
co4 = "#403d3d"

# Criação da janela principal
janela = Tk()
janela.title('POKEDEX')
janela.geometry('550x510')
janela.configure(bg='white')

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use('clam')

# Criando frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

# Nome
pok_nome = Label(frame_pokemon, text='PIKACHU', relief='flat', anchor=CENTER, font=('Fixedsys', 20), bg='white', fg='black')
pok_nome.place(x=12, y=15)

# Categoria
pok_categoria = Label(frame_pokemon, text='Eletrico', relief='flat', anchor=CENTER, font=('Ivy', 10), bg='white', fg='black')
pok_categoria.place(x=12, y=50)
pok_categoria.lift()

# ID
pok_id = Label(frame_pokemon, text='#025', relief='flat', anchor=CENTER, font=('Ivy', 10), bg='white', fg='black')
pok_id.place(x=12, y=75)

# Imagem
imagem_pokemon = Image.open('images/pikachu.png')
imagem_pokemon = imagem_pokemon.resize((238, 238))
imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

pok_imagem = Label(frame_pokemon, image=imagem_pokemon, relief='flat', bg='white', fg='black')
pok_imagem.place(x=60, y=50)

# Status
pok_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana', 20), bg='white', fg='black')
pok_status.place(x=15, y=310)

# HP
pok_hp = Label(janela, text='HP: 100', relief='flat', anchor=CENTER, font=('Verdana', 10), bg='white', fg=co4)
pok_hp.place(x=15, y=360)

# Ataque
pok_ataque = Label(janela, text='Ataque: 600', relief='flat', anchor=CENTER, font=('Verdana', 10), bg='white', fg=co4)
pok_ataque.place(x=15, y=385)

# Defesa
pok_defesa = Label(janela, text='Defesa: 100', relief='flat', anchor=CENTER, font=('Verdana', 10), bg='white', fg=co4)
pok_defesa.place(x=15, y=410)

# Velocidade
pok_velocidade = Label(janela, text='Velocidade: 100', relief='flat', anchor=CENTER, font=('Verdana', 10), bg='white', fg=co4)
pok_velocidade.place(x=15, y=435)

# Total
pok_total = Label(janela, text='Total: 100', relief='flat', anchor=CENTER, font=('Verdana', 10), bg='white', fg=co4)
pok_total.place(x=15, y=460)

# Habilidades
pok_habilidades = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana', 20), bg='white', fg=co4)
pok_habilidades.place(x=180, y=310)

# Habilidade1
pok_habilidade1 = Label(janela, text='Jato de água', relief='flat', anchor=CENTER, font=('Verdana', 10), bg='white', fg=co4)
pok_habilidade1.place(x=195, y=360)

# Habilidade2
pok_habilidade2 = Label(janela, text='Soco elétrico', relief='flat', anchor=CENTER, font=('Verdana', 10), bg='white', fg=co4)
pok_habilidade2.place(x=195, y=385)






'''# Criando uma lista de opções para o Combobox
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

botao1 = Button(janela, text="Sim!", command=botao_clicado)
botao1.place(relx=0.45, rely=0.20, anchor=CENTER)

botao2 = Button(janela, text="Não!", command=botao_clicado2)
botao2.place(relx=0.55, rely=0.20, anchor=CENTER)

# Entrada de dados
campo_entrada = Entry(janela, width=30)
campo_entrada.pack(pady=10)

botao_exibir = Button(janela, text='Exibir Entrada', command=exibir_entrada)
botao_exibir.pack()

resultado2 = Label(janela, text='')
resultado2.pack(pady=10)'''

# Inicia o loop principal da aplicação
janela.mainloop()
