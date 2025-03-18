from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from dados import *

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

def trocar_pokemon(i):
    global imagem_pokemon, pok_imagem

    # Tipo
    pok_nome['text'] = i
    pok_categoria['text'] = pokemon[i]['categoria'][1]
    pok_id['text'] = pokemon[i]['categoria'][0]

    # Imagem

    imagem_pokemon = pokemon[i]['categoria'][2]
    imagem_pokemon = Image.open(imagem_pokemon)
    imagem_pokemon = imagem_pokemon.resize((238, 238))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

    pok_imagem = Label(frame_pokemon, image=imagem_pokemon, relief='flat', bg='white', fg='black')
    pok_imagem.place(x=60, y=50)

# Nome
pok_nome = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys', 20), bg='white', fg='black')
pok_nome.place(x=12, y=15)

# Categoria
pok_categoria = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy', 10), bg='white', fg='black')
pok_categoria.place(x=12, y=50)
pok_categoria.lift()

# ID
pok_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy', 10), bg='white', fg='black')
pok_id.place(x=12, y=75)

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

# Criando botões
imagem_pokemon_1 = Image.open('images/cabeca-pikachu.png')
imagem_pokemon_1 = imagem_pokemon_1.resize((40, 40))
imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)

bot_pok_1 = Button(janela, command=lambda: trocar_pokemon('PIKACHU'), image=imagem_pokemon_1, text='Pikachu', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana', 12), bg='white', fg='black')
bot_pok_1.place(x=375, y=10)

imagem_pokemon_2 = Image.open('images/cabeca-bulbasaur.png')
imagem_pokemon_2 = imagem_pokemon_2.resize((40, 40))
imagem_pokemon_2 = ImageTk.PhotoImage(imagem_pokemon_2)

bot_pok_2 = Button(janela, command=lambda: trocar_pokemon('BULBASAUR'), image=imagem_pokemon_2, text='Bulbasaur', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana', 12), bg='white', fg='black')
bot_pok_2.place(x=375, y=65)

imagem_pokemon_3 = Image.open('images/cabeca-charmander.png')
imagem_pokemon_3 = imagem_pokemon_3.resize((40, 40))
imagem_pokemon_3 = ImageTk.PhotoImage(imagem_pokemon_3)

bot_pok_3 = Button(janela, command=lambda: trocar_pokemon('CHARMANDER'), image=imagem_pokemon_3, text='Charmander', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana', 12), bg='white', fg='black')
bot_pok_3.place(x=375, y=120)

imagem_pokemon_4 = Image.open('images/cabeca-gyarados.png')
imagem_pokemon_4 = imagem_pokemon_4.resize((40, 40))
imagem_pokemon_4 = ImageTk.PhotoImage(imagem_pokemon_4)

bot_pok_4 = Button(janela, command=lambda: trocar_pokemon('GYARADOS'), image=imagem_pokemon_4, text='Gyarados', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana', 12), bg='white', fg='black')
bot_pok_4.place(x=375, y=175)

imagem_pokemon_5 = Image.open('images/cabeca-gengar.png')
imagem_pokemon_5 = imagem_pokemon_5.resize((40, 40))
imagem_pokemon_5 = ImageTk.PhotoImage(imagem_pokemon_5)

bot_pok_5 = Button(janela, command=lambda: trocar_pokemon('GENGAR'), image=imagem_pokemon_5, text='Gengar', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana', 12), bg='white', fg='black')
bot_pok_5.place(x=375, y=230)

imagem_pokemon_6 = Image.open('images/cabeca-dragonite.png')
imagem_pokemon_6 = imagem_pokemon_6.resize((40, 40))
imagem_pokemon_6 = ImageTk.PhotoImage(imagem_pokemon_6)

bot_pok_6 = Button(janela, command=lambda: trocar_pokemon('DRAGONITE'), image=imagem_pokemon_6, text='Dragonite', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana', 12), bg='white', fg='black')
bot_pok_6.place(x=375, y=285)





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
