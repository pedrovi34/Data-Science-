import tkinter as tk
from tkinter import messagebox

# Lista de 20 perguntas avançadas de várias áreas de conhecimento
# Formato: (pergunta, [alternativa1, alternativa2, alternativa3, alternativa4], índice da resposta correta)
questoes = [
    # História - Primeira e Segunda Guerra Mundial, Crise de 1929 e Era Vargas
    ("1. Qual evento foi o estopim da Primeira Guerra Mundial?",
     ["Invasão da Polônia", "Assassinato do arquiduque Francisco Ferdinando", "Queda da Bastilha",
      "Declaração de independência dos EUA"],
     1),

    ("2. Qual tratado encerrou oficialmente a Primeira Guerra Mundial?",
     ["Tratado de Paris", "Tratado de Tordesilhas", "Tratado de Versalhes", "Tratado de Viena"],
     2),

    ("3. A Crise de 1929 teve início em qual país?",
     ["Alemanha", "Reino Unido", "França", "Estados Unidos"],
     3),

    ("4. Qual dos seguintes eventos marcou o início da Segunda Guerra Mundial?",
     ["Bombardeio de Pearl Harbor", "Invasão da Polônia", "Ataque à França", "O Dia D"],
     1),

    ("5. Durante o governo de Getúlio Vargas no Brasil, qual foi a política trabalhista estabelecida?",
     ["Livre mercado", "Justiça do Trabalho e CLT", "Privatizações", "Abertura econômica"],
     1),

    # Matemática - Derivadas e Integrais
    ("6. Qual é a derivada da função f(x) = 3x² + 2x + 1?",
     ["6x + 2", "3x²", "2x + 1", "3"],
     0),

    ("7. A integral indefinida de f(x) = x³ é:",
     ["x^4/4 + C", "3x²", "x^2/2 + C", "4x"],
     0),

    ("8. Qual é a integral definida de f(x) = x de 0 a 2?",
     ["1", "2", "4", "4/2"],
     2),

    ("9. A derivada da função f(x) = e^x é:",
     ["e^x", "x·e^x", "e^(x-1)", "1/e^x"],
     0),

    ("10. Qual é a derivada de f(x) = ln(x)?",
     ["1/x", "ln(x^2)", "x·ln(x)", "x"],
     0),

    # Biologia
    ("11. Qual é a unidade funcional dos rins?",
     ["Nefron", "Alvéolo", "Glândula", "Vilosidade"],
     0),

    ("12. Onde ocorre a fotossíntese nas células vegetais?",
     ["Mitocôndrias", "Ribossomos", "Cloroplastos", "Lisossomos"],
     2),

    ("13. Qual é o processo que leva à formação de gametas?",
     ["Meiose", "Mitose", "Fusão nuclear", "Transcrição"],
     0),

    ("14. Qual célula do sistema imunológico é conhecida por 'engolir' patógenos?",
     ["Hemácia", "Linfócito", "Neurônio", "Macrófago"],
     3),

    ("15. A divisão celular responsável pela regeneração de tecidos é chamada de:",
     ["Meiose", "Citocinese", "Mitose", "Duplicação"],
     2),

    # Química
    ("16. Qual o principal tipo de ligação química nas moléculas de água?",
     ["Iônica", "Metálica", "Covalente polar", "Covalente apolar"],
     2),

    ("17. Qual é a fórmula química do etanol?",
     ["CH4", "C2H5OH", "H2O", "C3H8"],
     1),

    ("18. Qual é o número atômico do carbono?",
     ["12", "14", "6", "8"],
     2),

    # Física
    ("19. Qual é a unidade de medida de carga elétrica no Sistema Internacional?",
     ["Joule", "Newton", "Coulomb", "Watt"],
     2),

    ("20. Qual é a terceira lei de Newton?",
     ["Inércia", "Ação e reação", "Força e massa", "Gravidade"],
     1)
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz de Ciências e Humanidades")
        self.root.geometry("600x500")

        # Variáveis de controle
        self.index_pergunta = 0
        self.pontuacao = 0

        # Label para a pergunta
        self.label_pergunta = tk.Label(root, text="", wraplength=500, font=("Arial", 16))
        self.label_pergunta.pack(pady=20)

        # Variável para armazenar a resposta escolhida
        self.resposta_selecionada = tk.IntVar()

        # Opções de resposta (Radio Buttons)
        self.opcoes_resposta = []
        for i in range(4):
            radio = tk.Radiobutton(root, text="", variable=self.resposta_selecionada, value=i, font=("Arial", 14))
            radio.pack(anchor="w")
            self.opcoes_resposta.append(radio)

        # Botão para confirmar a resposta
        self.botao_confirmar = tk.Button(root, text="Confirmar", command=self.verificar_resposta)
        self.botao_confirmar.pack(pady=20)

        # Carregar a primeira pergunta
        self.carregar_pergunta()

    def carregar_pergunta(self):
        pergunta, alternativas, _ = questoes[self.index_pergunta]
        self.label_pergunta.config(text=pergunta)
        for i, alternativa in enumerate(alternativas):
            self.opcoes_resposta[i].config(text=alternativa)
        self.resposta_selecionada.set(-1)

    def verificar_resposta(self):
        pergunta, alternativas, resposta_correta = questoes[self.index_pergunta]
        if self.resposta_selecionada.get() == resposta_correta:
            self.pontuacao += 1
            messagebox.showinfo("Resposta Correta", "Você acertou!")
        else:
            resposta_certa = alternativas[resposta_correta]
            messagebox.showinfo("Resposta Incorreta", f"Resposta correta: {resposta_certa}")

        self.index_pergunta += 1
        if self.index_pergunta < len(questoes):
            self.carregar_pergunta()
        else:
            self.exibir_resultado()

    def exibir_resultado(self):
        messagebox.showinfo("Resultado", f"Você acertou {self.pontuacao} de {len(questoes)} perguntas!")
        self.root.destroy()


# Configuração da janela principal
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
