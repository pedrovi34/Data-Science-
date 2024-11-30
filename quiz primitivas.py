import tkinter as tk
from tkinter import messagebox

# Dados do quiz
questions = [
    {"question": "Qual a primitiva de ∫xⁿ dx (n ≠ -1)?",
     "options": ["x^(n+1) / (n+1) + C", "ln|x| + C", "e^x + C"],
     "answer": "x^(n+1) / (n+1) + C"},
    {"question": "Qual a primitiva de ∫1/x dx?",
     "options": ["ln|x| + C", "e^x + C", "-cos(x) + C"],
     "answer": "ln|x| + C"},
    {"question": "Qual a primitiva de ∫e^x dx?",
     "options": ["e^x + C", "ln|x| + C", "sin(x) + C"],
     "answer": "e^x + C"},
    {"question": "Qual a primitiva de ∫sen(x) dx?",
     "options": ["-cos(x) + C", "tan(x) + C", "sin(x) + C"],
     "answer": "-cos(x) + C"},
    {"question": "Qual a primitiva de ∫cos(x) dx?",
     "options": ["sin(x) + C", "-cos(x) + C", "sec(x) + C"],
     "answer": "sin(x) + C"},
    {"question": "Qual a primitiva de ∫sec²(x) dx?",
     "options": ["tan(x) + C", "sec(x) + C", "cot(x) + C"],
     "answer": "tan(x) + C"},
    {"question": "Qual a primitiva de ∫sec(x)·tan(x) dx?",
     "options": ["sec(x) + C", "tan(x) + C", "cos(x) + C"],
     "answer": "sec(x) + C"},
    {"question": "Qual a primitiva de ∫cosec²(x) dx?",
     "options": ["-cot(x) + C", "tan(x) + C", "sec(x) + C"],
     "answer": "-cot(x) + C"},
    {"question": "Qual a primitiva de ∫cosec(x)·cot(x) dx?",
     "options": ["-cosec(x) + C", "cot(x) + C", "sec(x) + C"],
     "answer": "-cosec(x) + C"},
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz de Primitivas")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f8ff")
        self.score = 0
        self.current_question = 0

        # Título
        self.title_label = tk.Label(root, text="Quiz de Primitivas", font=("Arial", 20, "bold"), bg="#4682b4", fg="white", pady=10)
        self.title_label.pack(fill=tk.X)

        # Pergunta
        self.question_label = tk.Label(root, text="", font=("Arial", 16), bg="#f0f8ff", wraplength=550, justify="center")
        self.question_label.pack(pady=20)

        # Variável para rastrear a resposta escolhida
        self.selected_answer = tk.StringVar()

        # Botões de opção
        self.options_frame = tk.Frame(root, bg="#f0f8ff")
        self.options_frame.pack()

        self.radio_buttons = []
        for i in range(3):
            rb = tk.Radiobutton(self.options_frame, text="", variable=self.selected_answer, value="", font=("Arial", 14), bg="#f0f8ff", anchor="w", wraplength=500)
            rb.pack(anchor="w", pady=5)
            self.radio_buttons.append(rb)

        # Botão de próxima
        self.next_button = tk.Button(root, text="Confirmar", font=("Arial", 14, "bold"), bg="#4682b4", fg="white", command=self.check_answer)
        self.next_button.pack(pady=20)

        # Inicializar o quiz
        self.display_question()

    def display_question(self):
        # Exibir a pergunta atual
        q = questions[self.current_question]
        self.question_label.config(text=q["question"])
        self.selected_answer.set("")  # Resetar seleção

        # Atualizar as opções
        for i, option in enumerate(q["options"]):
            self.radio_buttons[i].config(text=option, value=option)

    def check_answer(self):
        # Verificar se uma opção foi selecionada
        if not self.selected_answer.get():
            messagebox.showwarning("Aviso", "Por favor, selecione uma resposta!")
            return

        # Verificar se a resposta está correta
        q = questions[self.current_question]
        if self.selected_answer.get() == q["answer"]:
            self.score += 1
            messagebox.showinfo("Correto!", "Você acertou!")
        else:
            messagebox.showerror("Errado!", f"Você errou!\nA resposta correta é: {q['answer']}")

        # Próxima pergunta ou finalizar
        self.current_question += 1
        if self.current_question < len(questions):
            self.display_question()
        else:
            self.finish_quiz()

    def finish_quiz(self):
        # Exibir pontuação final
        messagebox.showinfo("Fim do Quiz", f"Você concluiu o quiz!\nSua pontuação final foi: {self.score}/{len(questions)}")
        self.root.destroy()

# Criar a interface
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
