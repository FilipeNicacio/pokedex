from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sys
import tkinter as tk
from dados import *
import random

# Letra
co4 = "#403d3d"

janela = Tk()
janela.title('POKEDEX')
janela.geometry('550x510')
janela.configure(bg='red')

canvas = tk.Canvas(janela, width=550, height=510, bg='red')
canvas.pack()

# Círculo externo
canvas.create_oval(40, 40, 160, 160, fill="lightblue", outline="gray", width=2)

# Círculo interno
canvas.create_oval(50, 50, 150, 150, fill="blue")

# Luzes
canvas.create_oval(200, 50, 230, 80, fill="red", width=2)
canvas.create_oval(240, 50, 270, 80, fill="yellow", width=2)
canvas.create_oval(280, 50, 310, 80, fill="green", width=2)

# Quadrado principal
canvas.create_rectangle(30, 180, 510, 470, fill="red", outline="black", width=3)  # Borda preta e grossa

# Quadrado interno
canvas.create_rectangle(120, 450, 420, 435, fill="red", outline="black", width=2, stipple='gray12')

# Triângulo lateral
canvas.create_polygon(30, 300, 60, 330, 30, 360, fill="yellow", tags="triangulo")

# Adiciona o evento de clique ao triângulo
canvas.tag_bind("triangulo", "<Button-1>", lambda event: abrir_pokedex())


def get_resource_path(relative_path):
    try:
        # Para executáveis criados com PyInstaller
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def abrir_pokedex():

    # Altera a cor do triângulo para cinza claro
    canvas.itemconfig("triangulo", fill="lightgray")
    # Restaura a cor original após 100 milissegundos
    janela.after(300, lambda: canvas.itemconfig("triangulo", fill="yellow"))
    canvas.itemconfig("triangulo", fill="lightgray")

    janela.withdraw()

    janela2 = tk.Toplevel()
    janela2.title('POKEDEX')
    janela2.geometry('550x510')
    janela2.configure(bg='white')

    ttk.Separator(janela2, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

    style = ttk.Style(janela2)
    style.theme_use('clam')

    frame_pokemon = Frame(janela2, width=550, height=290, relief='flat')
    frame_pokemon.grid(row=1, column=0)

    def trocar_pokemon(i):

        global imagem_pokemon, pok_imagem

        # Tipo
        pok_nome['text'] = i
        pok_nome['bg'] = pokemon[i]['categoria'][3]
        pok_categoria['text'] = pokemon[i]['categoria'][1]
        pok_categoria['bg'] = pokemon[i]['categoria'][3]
        pok_id['text'] = pokemon[i]['categoria'][0]
        pok_id['bg'] = pokemon[i]['categoria'][3]
        frame_pokemon['bg'] = pokemon[i]['categoria'][3]

        # Imagem

        imagem_pokemon = pokemon[i]['categoria'][2]
        imagem_pokemon = Image.open(get_resource_path(imagem_pokemon))
        imagem_pokemon = imagem_pokemon.resize((238, 238))
        imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

        pok_imagem = Label(frame_pokemon, image=imagem_pokemon, relief='flat', fg='black')
        pok_imagem['bg'] = pokemon[i]['categoria'][3]
        pok_imagem.place(x=60, y=50)

        # Status

        pok_hp['text'] = pokemon[i]['status'][0]
        pok_ataque['text'] = pokemon[i]['status'][1]
        pok_defesa['text'] = pokemon[i]['status'][2]
        pok_velocidade['text'] = pokemon[i]['status'][3]
        pok_total['text'] = pokemon[i]['status'][4]

        # Habilidades

        pok_habilidade1['text'] = pokemon[i]['habilidades'][0]
        pok_habilidade2['text'] = pokemon[i]['habilidades'][1]

    # Nome
    pok_nome = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys', 20), bg='white',
                     fg='black')
    pok_nome.place(x=12, y=15)

    # Categoria
    pok_categoria = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy', 10), bg='white',
                          fg='black')
    pok_categoria.place(x=12, y=50)
    pok_categoria.lift()

    # ID
    pok_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy', 10), bg='white', fg='black')
    pok_id.place(x=12, y=75)

    # Status
    pok_status = Label(janela2, text='Status', relief='flat', anchor=CENTER, font=('Verdana', 20), bg='white',
                       fg='black')
    pok_status.place(x=15, y=310)

    # HP
    pok_hp = Label(janela2, text='', relief='flat', anchor=CENTER, font=('Verdana', 10), bg='white', fg=co4)
    pok_hp.place(x=15, y=360)

    # Ataque
    pok_ataque = Label(janela2, text='', relief='flat', anchor=CENTER, font=('Verdana', 10), bg='white', fg=co4)
    pok_ataque.place(x=15, y=385)

    # Defesa
    pok_defesa = Label(janela2, text='', relief='flat', anchor=CENTER, font=('Verdana', 10), bg='white', fg=co4)
    pok_defesa.place(x=15, y=410)

    # Velocidade
    pok_velocidade = Label(janela2, text='', relief='flat', anchor=CENTER, font=('Verdana', 10), bg='white', fg=co4)
    pok_velocidade.place(x=15, y=435)

    # Total
    pok_total = Label(janela2, text='', relief='flat', anchor=CENTER, font=('Verdana', 10), bg='white', fg=co4)
    pok_total.place(x=15, y=460)

    # Habilidades
    pok_habilidades = Label(janela2, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana', 20), bg='white',
                            fg=co4)
    pok_habilidades.place(x=180, y=310)

    # Habilidade1
    pok_habilidade1 = Label(janela2, text='', relief='flat', anchor=CENTER, font=('Verdana', 10), bg='white', fg=co4)
    pok_habilidade1.place(x=195, y=360)

    # Habilidade2
    pok_habilidade2 = Label(janela2, text='', relief='flat', anchor=CENTER, font=('Verdana', 10), bg='white', fg=co4)
    pok_habilidade2.place(x=195, y=385)

    # Criando botões
    imagem_pokemon_1 = Image.open(get_resource_path('images/cabeca-pikachu.png'))
    imagem_pokemon_1 = imagem_pokemon_1.resize((40, 40))
    imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)

    bot_pok_1 = Button(janela2, command=lambda: trocar_pokemon('PIKACHU'), image=imagem_pokemon_1, text='Pikachu',
                       width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5,
                       font=('Verdana', 12), bg='white', fg='black')
    bot_pok_1.place(x=375, y=10)

    imagem_pokemon_2 = Image.open(get_resource_path('images/cabeca-bulbasaur.png'))
    imagem_pokemon_2 = imagem_pokemon_2.resize((40, 40))
    imagem_pokemon_2 = ImageTk.PhotoImage(imagem_pokemon_2)

    bot_pok_2 = Button(janela2, command=lambda: trocar_pokemon('BULBASAUR'), image=imagem_pokemon_2, text='Bulbasaur',
                       width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5,
                       font=('Verdana', 12), bg='white', fg='black')
    bot_pok_2.place(x=375, y=65)

    imagem_pokemon_3 = Image.open(get_resource_path('images/cabeca-charmander.png'))
    imagem_pokemon_3 = imagem_pokemon_3.resize((40, 40))
    imagem_pokemon_3 = ImageTk.PhotoImage(imagem_pokemon_3)

    bot_pok_3 = Button(janela2, command=lambda: trocar_pokemon('CHARMANDER'), image=imagem_pokemon_3, text='Charmander',
                       width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5,
                       font=('Verdana', 12), bg='white', fg='black')
    bot_pok_3.place(x=375, y=120)

    imagem_pokemon_4 = Image.open(get_resource_path('images/cabeca-gyarados.png'))
    imagem_pokemon_4 = imagem_pokemon_4.resize((40, 40))
    imagem_pokemon_4 = ImageTk.PhotoImage(imagem_pokemon_4)

    bot_pok_4 = Button(janela2, command=lambda: trocar_pokemon('GYARADOS'), image=imagem_pokemon_4, text='Gyarados',
                       width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5,
                       font=('Verdana', 12), bg='white', fg='black')
    bot_pok_4.place(x=375, y=175)

    imagem_pokemon_5 = Image.open(get_resource_path('images/cabeca-gengar.png'))
    imagem_pokemon_5 = imagem_pokemon_5.resize((40, 40))
    imagem_pokemon_5 = ImageTk.PhotoImage(imagem_pokemon_5)

    bot_pok_5 = Button(janela2, command=lambda: trocar_pokemon('GENGAR'), image=imagem_pokemon_5, text='Gengar',
                       width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5,
                       font=('Verdana', 12), bg='white', fg='black')
    bot_pok_5.place(x=375, y=230)

    imagem_pokemon_6 = Image.open(get_resource_path('images/cabeca-dragonite.png'))
    imagem_pokemon_6 = imagem_pokemon_6.resize((40, 40))
    imagem_pokemon_6 = ImageTk.PhotoImage(imagem_pokemon_6)

    bot_pok_6 = Button(janela2, command=lambda: trocar_pokemon('DRAGONITE'), image=imagem_pokemon_6, text='Dragonite',
                       width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5,
                       font=('Verdana', 12), bg='white', fg='black')
    bot_pok_6.place(x=375, y=285)

    # Escolher pokemon inicial aleatoriamente
    lista_pokemon = ['DRAGONITE', 'GENGAR', 'CHARMANDER', 'BULBASAUR', 'PIKACHU', 'GYARADOS']
    pokemon_escolhido = random.sample(lista_pokemon, 1)
    trocar_pokemon(pokemon_escolhido[0])

    janela2.mainloop()


janela.mainloop()
