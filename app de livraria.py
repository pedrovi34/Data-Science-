import tkinter as tk
from tkinter import messagebox, simpledialog

class Livro:
    def __init__(self, titulo, autor, isbn, preco, editora, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.preco = preco
        self.editora = editora
        self.quantidade = quantidade

class Livraria:
    def __init__(self, root):
        self.livros = []
        self.root = root
        self.root.title("Sistema de Livraria")

        # Widgets principais
        self.label = tk.Label(root, text="Bem-vindo à Livraria", font=("Arial", 16))
        self.label.pack(pady=10)

        self.btn_cadastrar = tk.Button(root, text="Cadastrar Livro", command=self.cadastrar_livro, width=20)
        self.btn_cadastrar.pack(pady=5)

        self.btn_listar = tk.Button(root, text="Listar Livros", command=self.listar_livros, width=20)
        self.btn_listar.pack(pady=5)

        self.btn_pesquisar = tk.Button(root, text="Pesquisar Livro", command=self.pesquisar_livro, width=20)
        self.btn_pesquisar.pack(pady=5)

        self.btn_alterar = tk.Button(root, text="Alterar Livro", command=self.alterar_livro, width=20)
        self.btn_alterar.pack(pady=5)

        self.btn_remover = tk.Button(root, text="Remover Livro", command=self.remover_livro, width=20)
        self.btn_remover.pack(pady=5)

        self.btn_sair = tk.Button(root, text="Sair", command=root.quit, width=20)
        self.btn_sair.pack(pady=5)

    def cadastrar_livro(self):
        titulo = simpledialog.askstring("Cadastrar Livro", "Digite o título do livro:")
        if not titulo:
            return
        autor = simpledialog.askstring("Cadastrar Livro", "Digite o autor do livro:")
        isbn = simpledialog.askstring("Cadastrar Livro", "Digite o ISBN do livro:")
        preco = simpledialog.askfloat("Cadastrar Livro", "Digite o preço do livro:")
        editora = simpledialog.askstring("Cadastrar Livro", "Digite a editora do livro:")
        quantidade = simpledialog.askinteger("Cadastrar Livro", "Digite a quantidade em estoque:")
        livro = Livro(titulo, autor, isbn, preco, editora, quantidade)
        self.livros.append(livro)
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")

    def listar_livros(self):
        if not self.livros:
            messagebox.showinfo("Livros", "Não há livros cadastrados.")
            return
        lista = "\n".join([f"{i+1}. {livro.titulo} - {livro.autor} (ISBN: {livro.isbn})" for i, livro in enumerate(self.livros)])
        messagebox.showinfo("Lista de Livros", lista)

    def pesquisar_livro(self):
        busca = simpledialog.askstring("Pesquisar Livro", "Digite o título, autor ou ISBN do livro:")
        if not busca:
            return
        livros_encontrados = [
            livro for livro in self.livros if busca.lower() in livro.titulo.lower() or
            busca.lower() in livro.autor.lower() or busca.lower() == livro.isbn.lower()
        ]
        if livros_encontrados:
            lista = "\n".join([f"{i+1}. {livro.titulo} - {livro.autor} (ISBN: {livro.isbn})" for i, livro in enumerate(livros_encontrados)])
            messagebox.showinfo("Livros Encontrados", lista)
        else:
            messagebox.showinfo("Pesquisa", "Nenhum livro encontrado.")

    def alterar_livro(self):
        if not self.livros:
            messagebox.showinfo("Alterar Livro", "Não há livros cadastrados.")
            return
        self.listar_livros()
        indice = simpledialog.askinteger("Alterar Livro", "Digite o número do livro que deseja alterar:")
        if not indice or indice < 1 or indice > len(self.livros):
            messagebox.showerror("Erro", "Número inválido.")
            return
        livro = self.livros[indice - 1]
        novo_titulo = simpledialog.askstring("Alterar Livro", f"Digite o novo título (Atual: {livro.titulo}):")
        if novo_titulo:
            livro.titulo = novo_titulo
        novo_autor = simpledialog.askstring("Alterar Livro", f"Digite o novo autor (Atual: {livro.autor}):")
        if novo_autor:
            livro.autor = novo_autor
        novo_isbn = simpledialog.askstring("Alterar Livro", f"Digite o novo ISBN (Atual: {livro.isbn}):")
        if novo_isbn:
            livro.isbn = novo_isbn
        novo_preco = simpledialog.askfloat("Alterar Livro", f"Digite o novo preço (Atual: {livro.preco}):")
        if novo_preco:
            livro.preco = novo_preco
        nova_editora = simpledialog.askstring("Alterar Livro", f"Digite a nova editora (Atual: {livro.editora}):")
        if nova_editora:
            livro.editora = nova_editora
        nova_quantidade = simpledialog.askinteger("Alterar Livro", f"Digite a nova quantidade (Atual: {livro.quantidade}):")
        if nova_quantidade:
            livro.quantidade = nova_quantidade
        messagebox.showinfo("Sucesso", "Livro alterado com sucesso!")

    def remover_livro(self):
        if not self.livros:
            messagebox.showinfo("Remover Livro", "Não há livros cadastrados.")
            return
        self.listar_livros()
        indice = simpledialog.askinteger("Remover Livro", "Digite o número do livro que deseja remover:")
        if not indice or indice < 1 or indice > len(self.livros):
            messagebox.showerror("Erro", "Número inválido.")
            return
        del self.livros[indice - 1]
        messagebox.showinfo("Sucesso", "Livro removido com sucesso!")


root = tk.Tk()
livraria = Livraria(root)
root.mainloop()
