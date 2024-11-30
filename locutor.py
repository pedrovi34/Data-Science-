import librosa
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Carregar um áudio de exemplo
def load_audio_file(file_path):
    audio, sample_rate = librosa.load(file_path, sr=None)
    return audio, sample_rate

# Extrair características do áudio
def extract_features(audio, sample_rate):
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

# Função para carregar o dataset
def load_dataset(data_dir):
    features = []
    labels = []
    # Para cada arquivo de áudio no diretório, extraímos as features
    for file in os.listdir(data_dir):
        if file.endswith('.wav'):
            audio, sample_rate = load_audio_file(os.path.join(data_dir, file))
            mfccs = extract_features(audio, sample_rate)
            features.append(mfccs)
            # Supondo que o nome do locutor está no nome do arquivo
            label = file.split('_')[0]
            labels.append(label)
    return np.array(features), np.array(labels)

# Dividir os dados em treino e teste
X, y = load_dataset('diretorio_dos_arquivos_de_audio')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de deep learning
model = tf.keras.Sequential([
    tf.keras.layers.Dense(256, input_shape=(X_train.shape[1],), activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(len(set(y)), activation='softmax') # Saída para classificação
])

# Compilar o modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Treinar o modelo
model.fit(X_train, y_train, epochs=30, batch_size=32, validation_data=(X_test, y_test))

# Avaliar o modelo
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Acurácia no conjunto de teste: {test_acc}")
