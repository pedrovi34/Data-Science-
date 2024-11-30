import tkinter as tk
from tkinter import messagebox

class ChurrascoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Churrasco - Lista de Contribuições")
        self.master.geometry("400x400")

        # Lista de participantes e itens
        self.contribuicoes = []

        # Criação da interface
        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)

        self.label = tk.Label(self.frame, text="Adicionar Participante e Item:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry_participante = self.create_entry(self.frame, "Nome do Participante")
        self.entry_item = self.create_entry(self.frame, "Item a Ser Levado")
        self.entry_preco = self.create_entry(self.frame, "Preço do Item (R$)")

        # Cores do arco-íris
        rainbow_colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#00FFFF", "#0000FF", "#4B0082"]

        self.add_button = tk.Button(self.frame, text="Adicionar", command=self.adicionar, bg=rainbow_colors[0], font=("Arial", 12), width=20)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.frame, text="Remover", command=self.remover, bg=rainbow_colors[1], font=("Arial", 12), width=20)
        self.remove_button.pack(pady=5)

        self.lista_box = tk.Listbox(self.frame, width=50, height=10, font=("Arial", 12))
        self.lista_box.pack(pady=5)

        self.show_button = tk.Button(self.frame, text="Mostrar Contribuições", command=self.mostrar_contribuicoes, bg=rainbow_colors[2], font=("Arial", 12), width=20)
        self.show_button.pack(pady=5)

    def create_entry(self, parent, placeholder):
        entry = tk.Entry(parent, width=40, font=("Arial", 12))
        entry.pack(pady=5)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda e: self.on_entry_click(entry, placeholder))
        entry.bind("<FocusOut>", lambda e: self.on_focusout(entry, placeholder))
        return entry

    def on_entry_click(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)  # Remove o placeholder
            entry.config(fg='black')  # Muda a cor do texto

    def on_focusout(self, entry, placeholder):
        if entry.get() == '':
            entry.insert(0, placeholder)  # Retorna o placeholder
            entry.config(fg='grey')  # Muda a cor do texto de placeholder

    def adicionar(self):
        nome = self.entry_participante.get()
        item = self.entry_item.get()
        preco = self.entry_preco.get()

        if nome and item and preco and nome != "Nome do Participante" and item != "Item a Ser Levado" and preco != "Preço do Item (R$)":
            self.contribuicoes.append((nome, item, preco))
            self.lista_box.insert(tk.END, f"{nome} - {item} - R$ {preco}")
            self.entry_participante.delete(0, tk.END)
            self.entry_item.delete(0, tk.END)
            self.entry_preco.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos corretamente.")

    def remover(self):
        try:
            selected_index = self.lista_box.curselection()[0]
            self.lista_box.delete(selected_index)
            del self.contribuicoes[selected_index]
        except IndexError:
            messagebox.showwarning("Seleção inválida", "Por favor, selecione um item para remover.")

    def mostrar_contribuicoes(self):
        contrib = "\n".join([f"{nome} - {item} - R$ {preco}" for nome, item, preco in self.contribuicoes])
        if contrib:
            messagebox.showinfo("Contribuições", contrib)
        else:
            messagebox.showinfo("Contribuições", "Nenhuma contribuição registrada.")

# Criar a janela principal
root = tk.Tk()
app = ChurrascoApp(root)

# Iniciar a aplicação
root.mainloop()
