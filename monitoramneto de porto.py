import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import cv2
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


# Parte 1: Modelo CNN para Detecção de Contêineres

# Função para carregar os dados de imagens
def load_image_data(data_dir):
    images = []
    labels = []
    for label, class_dir in enumerate(os.listdir(data_dir)):
        for image_file in os.listdir(os.path.join(data_dir, class_dir)):
            image_path = os.path.join(data_dir, class_dir, image_file)
            image = cv2.imread(image_path)
            image = cv2.resize(image, (128, 128))  # Redimensiona para 128x128 pixels
            images.append(image)
            labels.append(label)
    images = np.array(images)
    labels = np.array(labels)
    return images, labels


# Carregar o dataset de contêineres
data_dir = 'dataset_conteineres'  # Substitua pelo seu dataset
X_img, y_img = load_image_data(data_dir)
X_img = X_img / 255.0  # Normalizando os dados

# Dividir o dataset em treino e teste
X_img_train, X_img_test, y_img_train, y_img_test = train_test_split(X_img, y_img, test_size=0.2, random_state=42)

# Construir o modelo CNN para detecção de contêineres
model_cnn = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Saída binária: contêiner ou não
])

# Compilar e treinar o modelo
model_cnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model_cnn.fit(X_img_train, y_img_train, epochs=5, validation_data=(X_img_test, y_img_test))
model_cnn.save('modelo_conteineres.h5')


# Função de detecção de contêiner em tempo real
def detectar_conteiner(frame):
    image_resized = cv2.resize(frame, (128, 128))
    image_array = np.expand_dims(image_resized, axis=0)
    pred = model_cnn.predict(image_array)
    return pred[0][0] > 0.5  # Retorna True se for contêiner


# Parte 2: Previsão de Demanda de Contêineres usando LSTM

# Gerar dados sintéticos de demanda para exemplo
data = {'dias': np.arange(0, 1000), 'demanda': np.sin(np.arange(0, 1000) * 0.01) * 100 + 500}
df = pd.DataFrame(data)

# Preprocessamento de dados para LSTM
scaler = MinMaxScaler()
df['demanda_scaled'] = scaler.fit_transform(df['demanda'].values.reshape(-1, 1))


# Criar sequência de treinamento
def create_sequences(data, seq_length):
    sequences = []
    labels = []
    for i in range(len(data) - seq_length):
        sequences.append(data[i:i + seq_length])
        labels.append(data[i + seq_length])
    return np.array(sequences), np.array(labels)


sequence_length = 30  # Número de dias anteriores para prever a demanda
X_seq, y_seq = create_sequences(df['demanda_scaled'], sequence_length)

# Dividir dados em treino e teste
X_seq_train, X_seq_test, y_seq_train, y_seq_test = train_test_split(X_seq, y_seq, test_size=0.2, random_state=42)

# Criar o modelo LSTM para previsão de demanda
model_lstm = models.Sequential([
    layers.LSTM(50, return_sequences=True, input_shape=(X_seq_train.shape[1], 1)),
    layers.LSTM(50),
    layers.Dense(1)
])

# Compilar e treinar o modelo
model_lstm.compile(optimizer='adam', loss='mean_squared_error')
model_lstm.fit(X_seq_train, y_seq_train, epochs=10, validation_data=(X_seq_test, y_seq_test))
model_lstm.save('modelo_demanda_lstm.h5')


# Função de previsão de demanda
def prever_demanda(dados_recentes):
    dados_recentes = scaler.transform(np.array(dados_recentes).reshape(-1, 1))
    dados_recentes = np.expand_dims(dados_recentes, axis=0)
    pred = model_lstm.predict(dados_recentes)
    return scaler.inverse_transform(pred)[0][0]


# Parte 3: Manutenção Preditiva de Equipamentos

# Dados sintéticos de falhas de equipamentos
data_manutencao = {'uso_horas': np.random.randint(0, 10000, 1000),
                   'temperatura': np.random.uniform(20, 100, 1000),
                   'vibracao': np.random.uniform(0.1, 1.0, 1000),
                   'falha': np.random.randint(0, 2, 1000)}

df_manutencao = pd.DataFrame(data_manutencao)

# Dividir dados
X_man = df_manutencao[['uso_horas', 'temperatura', 'vibracao']]
y_man = df_manutencao['falha']

X_man_train, X_man_test, y_man_train, y_man_test = train_test_split(X_man, y_man, test_size=0.2, random_state=42)

# Criar o modelo de rede neural para manutenção preditiva
model_man = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_man_train.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Compilar e treinar o modelo
model_man.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model_man.fit(X_man_train, y_man_train, epochs=10, validation_data=(X_man_test, y_man_test))
model_man.save('modelo_manutencao.h5')


# Função de previsão de falhas
def prever_falha(uso_horas, temperatura, vibracao):
    pred = model_man.predict(np.array([[uso_horas, temperatura, vibracao]]))
    return pred[0][0] > 0.5  # Retorna True se é provável que falhe


# Parte 4: Algoritmo de Busca Tabu para Otimização de Rotas

# Função para calcular a distância Euclidiana
def calcular_distancia(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Implementação do Algoritmo de Busca Tabu
def busca_tabu(containers, max_iter=100, tabu_tamanho=10):
    melhor_rota = list(containers.keys())
    melhor_custo = calcular_custo(melhor_rota)
    tabu_list = []

    for iteracao in range(max_iter):
        vizinhos = []
        for i in range(len(melhor_rota)):
            for j in range(i + 1, len(melhor_rota)):
                vizinho = melhor_rota.copy()
                vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
                if vizinho not in tabu_list:
                    vizinhos.append(vizinho)

        melhor_vizinho = None
        melhor_custo_vizinho = float('inf')

        for vizinho in vizinhos:
            custo_vizinho = calcular_custo(vizinho)
            if custo_vizinho < melhor_custo_vizinho:
                melhor_custo_vizinho = custo_vizinho
                melhor_vizinho = vizinho

        if melhor_vizinho and melhor_custo_vizinho < melhor_custo:
            melhor_rota = melhor_vizinho
            melhor_custo = melhor_custo_vizinho
            tabu_list.append(melhor_rota)
            if len(tabu_list) > tabu_tamanho:
                tabu_list.pop(0)  # Remove o elemento mais antigo

    return melhor_rota, melhor_custo


# Função para calcular o custo total de uma rota
def calcular_custo(rota):
    # Supondo que cada contêiner tem coordenadas (x, y)
    custo_total = 0
    for i in range(len(rota) - 1):
        custo_total += calcular_distancia(containers[rota[i]], containers[rota[i + 1]])
    return custo_total


# Parte 5: Integração do Sistema em Tempo Real

cap = cv2.VideoCapture(0)  # Webcam para simulação de detecção de contêineres

# Exemplo de contêineres com suas coordenadas
containers = {
    'container_1': (0, 0),
    'container_2': (1, 2),
    'container_3': (3, 1),
    'container_4': (4, 3),
    # Adicione mais contêineres conforme necessário
}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if detectar_conteiner(frame):
        cv2.putText(frame, "Contêiner Detectado", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Executa a busca tabu para otimização de movimentação
        melhor_rota, custo = busca_tabu(containers)
        print(f"Melhor Rota: {melhor_rota} com Custo: {custo}")

    # Exemplo de previsão de demanda com os últimos 30 dias
    demanda_prevista = prever_demanda(df['demanda'][-30:])
    print(f"Previsão de Demanda: {demanda_prevista}")

    # Exemplo de manutenção preditiva
    falha_prevista = prever_falha(5000, 80, 0.5)  # Dados de exemplo
    print(f"Falha Prevista: {'Sim' if falha_prevista else 'Não'}")

    cv2.imshow('Detecção de Contêineres', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
