# Importação das bibliotecas necessárias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# Estilização dos gráficos
sns.set(style="whitegrid")

# Expansão do conjunto de dados para incluir mais doenças
data = {
    'chuvas_mm': [100, 80, 120, 200, 50, 20, 150, 80, 200, 300, 90, 60, 250],
    'temperatura_celsius': [30, 28, 32, 33, 29, 27, 31, 29, 33, 35, 30, 26, 34],
    'umidade_relativa': [70, 65, 80, 90, 60, 50, 85, 70, 95, 90, 75, 68, 88],
    'incidencia_dengue': [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
    'incidencia_chikungunya': [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    'incidencia_febre_amarela': [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    'incidencia_asma': [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1],
    'incidencia_bronquite': [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Exibição do conjunto de dados resumido
print("Conjunto de dados simulados (primeiros 5 registros):\n", df.head())

# Separação dos dados em variáveis preditoras (X) e variáveis alvo (y)
X = df[['chuvas_mm', 'temperatura_celsius', 'umidade_relativa']]
y = df[['incidencia_dengue', 'incidencia_chikungunya', 'incidencia_febre_amarela', 'incidencia_asma', 'incidencia_bronquite']]

# Divisão dos dados em treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criação do modelo de Random Forest para cada doença
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Previsão nos dados de teste
y_pred = model.predict(X_test)

# Avaliação do modelo
accuracy = model.score(X_test, y_test)
print(f'Acurácia do modelo: {accuracy:.2f}')

# Visualizando a matriz de confusão para cada doença (heatmap)
from sklearn.metrics import multilabel_confusion_matrix

mcm = multilabel_confusion_matrix(y_test, y_pred)

# Gráfico de matriz de confusão para cada doença
fig, axs = plt.subplots(2, 3, figsize=(15, 10))
diseases = ['Dengue', 'Chikungunya', 'Febre Amarela', 'Asma', 'Bronquite']
for i, ax in enumerate(axs.flat):
    if i < len(diseases):
        sns.heatmap(mcm[i], annot=True, fmt="d", cmap="Blues", ax=ax)
        ax.set_title(f'Matriz de Confusão - {diseases[i]}')
        ax.set_xlabel('Previsão')
        ax.set_ylabel('Real')

plt.tight_layout()
plt.show()

# Visualização da importância das variáveis no modelo
importances = model.feature_importances_
features = X.columns

plt.figure(figsize=(10, 6))
sns.barplot(x=importances, y=features, palette="Blues_d")
plt.title('Importância das Variáveis no Modelo Preditivo')
plt.xlabel('Importância')
plt.ylabel('Variável')
plt.show()

# Previsão com novos dados simulados
novos_dados = pd.DataFrame({
    'chuvas_mm': [250, 50, 180],
    'temperatura_celsius': [31, 27, 34],
    'umidade_relativa': [88, 45, 92]
})

# Prevendo surto para todas as doenças com os novos dados
previsao_surto = model.predict(novos_dados)
print("\nPrevisão para novos dados (0 = Sem surto, 1 = Com surto):")
for i, prev in enumerate(previsao_surto):
    print(f"Caso {i+1}: Dengue: {prev[0]}, Chikungunya: {prev[1]}, Febre Amarela: {prev[2]}, Asma: {prev[3]}, Bronquite: {prev[4]}")

# Criando um DataFrame para visualização geoespacial
localizacoes = pd.DataFrame({
    'latitude': [-7.11532, -8.04756, -3.71722],
    'longitude': [-34.861, -34.876, -38.543],
    'cidade': ['João Pessoa', 'Recife', 'Fortaleza'],
    'previsao_dengue': previsao_surto[:, 0],
    'previsao_chikungunya': previsao_surto[:, 1],
    'previsao_febre_amarela': previsao_surto[:, 2],
    'previsao_asma': previsao_surto[:, 3],
    'previsao_bronquite': previsao_surto[:, 4]
})

# Criando um mapa interativo com a biblioteca Folium
mapa = folium.Map(location=[-5.7945, -35.211], zoom_start=6)

# Adicionando marcadores no mapa para cada cidade e risco de doença
for i, row in localizacoes.iterrows():
    popup_text = f"<b>{row['cidade']}</b><br>Dengue: {row['previsao_dengue']}<br>Chikungunya: {row['previsao_chikungunya']}<br>Febre Amarela: {row['previsao_febre_amarela']}<br>Asma: {row['previsao_asma']}<br>Bronquite: {row['previsao_bronquite']}"
    folium.Marker(location=[row['latitude'], row['longitude']],
                  popup=popup_text,
                  icon=folium.Icon(color="red" if row['previsao_dengue'] else "green")).add_to(mapa)

# Exibir o mapa
mapa.save('mapa_interativo.html')
print("Mapa interativo salvo como 'mapa_interativo.html'. Abra o arquivo no seu navegador para visualizar.")
d