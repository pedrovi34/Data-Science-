import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


# Simulação de dados logísticos
def simulate_data():
    data = {
        'Distância (km)': np.random.randint(100, 2000, size=1000),
        'Peso da Carga (Ton)': np.random.randint(500, 20000, size=1000),
        'Capacidade Vagão (%)': np.random.randint(50, 100, size=1000),
        'Velocidade Média (km/h)': np.random.randint(40, 80, size=1000),
        'Condição Climática (0=Bom, 1=Ruim)': np.random.choice([0, 1], size=1000),
        'Atraso': np.random.choice([0, 1], size=1000)  # Garantindo que a coluna 'Atraso' exista
    }
    return pd.DataFrame(data)


# Função para treinar o modelo
def train_model(data):
    X = data.drop('Atraso', axis=1)  # Garantindo que 'Atraso' esteja presente no DataFrame
    y = data['Atraso']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    return model, scaler


# Função para prever atrasos
def predict_delay(model, inputs):
    return model.predict([inputs])[0]


# Função para salvar histórico
def save_to_excel(data):
    data.to_excel("logistica_vale.xlsx", index=False)


# Interface gráfica com Tkinter
def create_interface():
    root = tk.Tk()
    root.title("Sistema de Previsão Logística Vale")

    # Labels e campos de entrada
    labels = ['Distância (km)', 'Peso da Carga (Ton)', 'Capacidade Vagão (%)', 'Velocidade Média (km/h)',
              'Condição Climática (0=Bom, 1=Ruim)']
    entries = []

    for label_text in labels:
        label = tk.Label(root, text=label_text)
        label.pack()
        entry = tk.Entry(root)
        entry.pack()
        entries.append(entry)

    # Função para prever e mostrar resultado
    def predict():
        inputs = [float(entry.get()) for entry in entries]
        scaled_inputs = scaler.transform([inputs])
        result = predict_delay(model, scaled_inputs[0])
        result_text = "Atraso previsto!" if result == 1 else "Sem atraso previsto."
        messagebox.showinfo("Previsão", result_text)

    # Botão de previsão
    button = tk.Button(root, text="Prever Atraso", command=predict)
    button.pack()

    root.mainloop()


# Gerando e treinando o modelo com dados simulados
data = simulate_data()  # Simulação de dados corrigida
model, scaler = train_model(data)

# Criando a interface
create_interface()
