import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os

# Função para carregar dados fictícios
def load_data():
    data = {
        'Carga (Toneladas)': np.random.randint(500, 10000, size=200),
        'Distância (Km)': np.random.randint(50, 2000, size=200),
        'Tempo Estimado (Dias)': np.random.randint(1, 30, size=200),
        'Tipo de Carga': np.random.choice([0, 1], size=200),  # 0 = minério, 1 = contêiner
        'Atraso': np.random.choice([0, 1], size=200)  # 0 = sem atraso, 1 = com atraso
    }
    return pd.DataFrame(data)

# Função para salvar os dados no Excel
def save_to_excel(data, file_name="logistica_data.xlsx"):
    if os.path.exists(file_name):
        existing_data = pd.read_excel(file_name)
        data = pd.concat([existing_data, data], ignore_index=True)
    data.to_excel(file_name, index=False)

# Função para treinar o modelo de Machine Learning
def train_model_ml(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Função para fazer a previsão
def predict_ml(model, inputs):
    return model.predict([inputs])[0]

# Função para prever e salvar no Excel
def predict_and_save():
    try:
        inputs = [float(entry.get()) for entry in entries]
        scaled_inputs = scaler.transform([inputs])
        result = predict_ml(ml_model, scaled_inputs[0])
        outcome_text = "Atraso previsto!" if result == 1 else "Sem atraso previsto."

        data_dict = {field: [entry.get()] for field, entry in zip(fields, entries)}
        data_dict['Previsão'] = [outcome_text]
        new_data = pd.DataFrame(data_dict)
        save_to_excel(new_data)

        messagebox.showinfo("Resultado", outcome_text)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro nos dados de entrada: {e}")

# Função para limpar os campos de entrada
def clear_fields():
    for entry in entries:
        entry.delete(0, tk.END)

# Função para exibir o histórico de dados do Excel
def show_data():
    try:
        data = pd.read_excel("logistica_data.xlsx")
        table_window = tk.Toplevel(root)
        table_window.title("Histórico de Dados")
        tree = ttk.Treeview(table_window, columns=list(data.columns), show="headings")
        tree.pack(fill="both", expand=True)

        for col in data.columns:
            tree.heading(col, text=col)

        for index, row in data.iterrows():
            tree.insert("", tk.END, values=list(row))

    except FileNotFoundError:
        messagebox.showerror("Erro", "Nenhum histórico de dados encontrado.")

# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Previsão de Eficiência Logística")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

label_title = tk.Label(root, text="Previsão de Eficiência Logística", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
label_title.pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

fields = ['Carga (Toneladas)', 'Distância (Km)', 'Tempo Estimado (Dias)', 'Tipo de Carga (0 = Minério, 1 = Contêiner)']
entries = []

for i, field in enumerate(fields):
    label = tk.Label(frame, text=field, font=("Arial", 12), bg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(frame, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

button_predict = tk.Button(root, text="Prever Atraso", font=("Arial", 14), bg="#4CAF50", fg="white", command=predict_and_save)
button_predict.pack(pady=10)

button_clear = tk.Button(root, text="Limpar Campos", font=("Arial", 12), bg="#f44336", fg="white", command=clear_fields)
button_clear.pack(pady=10)

button_view_data = tk.Button(root, text="Ver Histórico", font=("Arial", 12), bg="#2196F3", fg="white", command=show_data)
button_view_data.pack(pady=10)

# Carregar e preparar os dados
data = load_data()
X = data.drop('Atraso', axis=1).values
y = data['Atraso'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

ml_model = train_model_ml(X_train, y_train)

root.mainloop()
