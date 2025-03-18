from tkinter import *
from tkinter import Canvas
import tkinter as tk
import subprocess
import sys

def clique_triangulo(event):
    subprocess.Popen([sys.executable, "pokedex.py"])
    # Altera a cor do triângulo para cinza claro
    canvas.itemconfig("triangulo", fill="lightgray")
    # Restaura a cor original após 100 milissegundos
    janela.after(100, lambda: canvas.itemconfig("triangulo", fill="yellow"))

janela = tk.Tk()
janela.title = 'HOME'
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
canvas.tag_bind("triangulo", "<Button-1>", clique_triangulo)

janela.mainloop()
