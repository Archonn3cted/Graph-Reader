import tkinter as tk
from tkinter import filedialog
from dijkstra import Grafo
from tkinter import *

# Interface do Usuário
class Aplicacao(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("TSP SOLVERS")
        self.master.geometry("400x300")
        self.pack()

        self.grid(sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(self, borderwidth=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Adicionar um scrollbar para rolar verticalmente o canvas
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        # Adicionar um scrollbar para rolar horizontalmente o canvas
        self.scrollbar_x = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.scrollbar_x.grid(row=1, column=0, sticky="ew")
        self.canvas.config(xscrollcommand=self.scrollbar_x.set)

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.adicionar_elementos()

        self.frame.bind("<Configure>", self.atualizar_scroll)

    def adicionar_elementos(self):

        self.titulo = tk.Label(self.frame, text="Implementação do Algoritmo de Dijkstra", font="bold")
        self.titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.botaoSelecionarArquivo = tk.Button(self.frame, text="Selecionar um Arquivo", command=self.selecionarArquivo)
        self.botaoSelecionarArquivo.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

        self.rotuloCaminhoArquivo = tk.Label(self.frame, text="Nenhum arquivo selecionado.")
        self.rotuloCaminhoArquivo.grid(row=2, columnspan=2, column=0, padx=20, pady=10)

        self.rotuloConteudoArquivo = tk.Label(self.frame, text="")
        self.rotuloConteudoArquivo.grid(row=3, columnspan=2, column=0, padx=20, pady=10)

        self.rotuloVerticeOrigem = tk.Label(self.frame, text="Digite o vértice de origem:")
        self.rotuloVerticeOrigem.grid(row=4, column=0, padx=20, pady=10)

        self.entradaVerticeOrigem = tk.Entry(self.frame)
        self.entradaVerticeOrigem.grid(row=4, column=1, padx=20, pady=10)

        self.botaoExecutarAcao = tk.Button(self.frame, text="Executar Ação", state="disabled", command=self.executarAcao)
        self.botaoExecutarAcao.grid(row=5, column=0, columnspan=2, padx=20, pady=20)

        self.botaoSair = tk.Button(self.frame, text="Sair", command=self.master.quit)
        self.botaoSair.grid(row=6, column=0, columnspan=2, padx=20, pady=20)

    def selecionarArquivo(self):
        caminhoArquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
        self.rotuloCaminhoArquivo.config(text=caminhoArquivo)

        with open(caminhoArquivo, "r") as arquivo:
            conteudoArquivo = arquivo.read()
            self.rotuloConteudoArquivo.config(text=conteudoArquivo)

            self.matrizAdjacencia = []
            for linha in conteudoArquivo.splitlines():
                valores = [int(valor) for valor in linha.strip().split()]
                self.matrizAdjacencia.append(valores)

        self.botaoExecutarAcao.config(state="normal")

    def executarAcao(self):
        numVertices = len(self.matrizAdjacencia)
        print("Número de vértices:", numVertices)
        print("Matriz de adjacência:")
        for linha in self.matrizAdjacencia:
            print(linha)

        grafo = Grafo(numVertices)

        for i in range(numVertices):
            for j in range(numVertices):
                if self.matrizAdjacencia[i][j] > 0:
                    grafo.adicionarAresta(i, j, self.matrizAdjacencia[i][j])

        origem = int(self.entradaVerticeOrigem.get())
        grafo.dijkstra(origem)

    def atualizar_scroll(self, event):
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

root = tk.Tk()
app = Aplicacao(master=root)
app.mainloop()