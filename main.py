import tkinter as tk
import tsp
from tkinter import *

def base_escolhida(arquivo):
    if arquivo == "att48.tsp":
        tsp.grafo_att()
    elif arquivo == "dantzig42.tsp":
        tsp.grafo_dant()
    elif arquivo == "fri26.tsp":
        tsp.grafo_fri()
    elif arquivo == "gr17.tsp":
        tsp.grafo_gr17()
    elif arquivo == "p01.tsp":
        tsp.grafo_p01()
    else:
        Message(root,text="Arquivo inválido. Por favor, escolha um arquivo válido")

arquivo = ["att48.tsp", "dantzig42.tsp", "fri26.tsp", "gr17.tsp", "p01.tsp"]

root = tk.Tk()
root.title("Info Grafo")

var = StringVar(root)
var.set("Escolha a base de dados")

menu = OptionMenu(root, var, *arquivo, command=base_escolhida)
menu.pack()

nome_label = tk.Label(root, text="Informações encontram-se no terminal!")
nome_label.pack()

root.mainloop()