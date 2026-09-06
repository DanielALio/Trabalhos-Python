import tkinter as tk #Importa a biblioteca da janela
from dominio.livro import Livro #Importa as 3 classes em dominio
from dominio.usuario import Usuario
from dominio.emprestimo import Emprestimo

#Declaração do acervo
acervo = [
    Livro("Through The Fire and Flames Carry on", "Dragon Force", 2014),
    Livro("Cry Thunder", "Carlos Crazzy", 2023),
    Livro("The life Snake", "Augusto Marcos", 2025)
]

#Declaração da lista de emprestímos
emprestimos = []
#Criação do usuário
usuario = Usuario("Eric", "695487")

janela = tk.Tk() #Gera a janela
janela.title("Biblioteca") #Título da janela
janela.geometry("750x600") #Tamanho da janela

tk.Label(janela, text="Acervo", font=("Arial", 14)).pack(pady=6) #Texto principal da janela
lista = tk.Listbox(janela, width=52, height=6) #Cria uma caixa de lista
#Insere os livros do acervo na lista já criada
for livro in acervo:
    lista.insert(tk.END, str(livro)) #tk.END = no fim da lista
lista.pack(padx=10)

campo = tk.Entry(janela, width=34)
campo.pack(pady=8) #Pack formata o botão ou campo

resultado = tk.Label(janela, text="", fg="blue") #Adiciona texto 

def emprestar():
    procurado = campo.get()

    escolhido = None
    for livro in acervo:
        if livro.titulo.lower() == procurado.lower():
            escolhido = livro

    if escolhido == None:
        resultado.config(text="Não está no acervo.", fg="red")
        return

    emprestimo = Emprestimo(escolhido, usuario, "27/09/2026")
    emprestimos.append(emprestimo)
    resultado.config(text="Emprestado: " + str(emprestimo), fg="blue")

def devolver():
    if not emprestimos:
        resultado.config(text="Não há emprestimo.", fg="red")
        return

    emprestimo = emprestimos[-1]
    try:
        emprestimo.devolver()
        resultado.config(text="Devolvido: " + str(emprestimo), fg="Blue")
    except ValueError as erro:
        resultado.config(text=str(erro), fg="red")

tk.Button(janela, text="Emprestar", command=emprestar).pack() #Cria o botão de emprestar
tk.Button(janela, text="Devolver", command=devolver).pack() #Cria o botão de devolver
resultado.pack(pady=6)

titulo_secao = tk.Label(janela, text="Cadastrar livro", font=("Arial", 12))
titulo_secao.pack(pady=(10, 4))

formulario = tk.Frame(janela)
formulario.pack()

tk.Label(formulario, text="Titulo: ").grid(row=1, column=0, sticky="e")
campo_titulo = tk.Entry(formulario, width=28)
campo_titulo.grid(row=1, column=1, pady=2)

tk.Label(formulario, text="Autor: ").grid(row=2, column=0, sticky="e")
campo_autor = tk.Entry(formulario, width=28)
campo_autor.grid(row=2, column=1, pady=2)

tk.Label(formulario, text="Data de lançamento: ").grid(row=3, column=0, sticky="e")
campo_ano = tk.Entry(formulario, width=28)
campo_ano.grid(row=3, column=1, pady=2)

def atualizar_lista():
    lista.delete(0, tk.END)
    for livro in acervo:
        lista.insert(tk.END, str(livro))

def cadastrar():
    titulo = campo_titulo.get()
    autor = campo_autor.get()
    ano = campo_ano.get()

    try:
        livro = Livro(titulo, autor, int(ano))
        acervo.append(livro)
        atualizar_lista()
        campo_titulo.delete(0, tk.END)
        campo_autor.delete(0, tk.END)
        campo_ano.delete(0, tk.END)
        resultado.config(text=f"Livro cadastrado: {titulo}/{autor}/{ano}", fg="blue")
    except ValueError as erro:
        resultado.config(text=f"Erro: {str(erro)}", fg="red")   

tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=6)

janela.mainloop()