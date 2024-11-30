import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay

# Dados da Matriz de Confusão SVM
conf_matrix = np.array([[0, 0, 0],
                        [69, 0, 0],
                        [0, 0, 66]])

# Plotar a matriz de confusão
fig, ax = plt.subplots(figsize=(6, 6))
ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=["-1", "0", "1"]).plot(ax=ax)
plt.title("Confusão da matriz SVM")
plt.show()

# Dados do relatório de classificação SVM
labels = ['-1', '0', '1']
precision = [0.0, 0.0, 1.0]
recall = [0.0, 0.0, 1.0]
f1_score = [0.0, 0.0, 1.0]

# Gráficos de Precisão, Recall e F1-Score
x = np.arange(len(labels))

fig, ax = plt.subplots(figsize=(8, 6))

bar_width = 0.2
ax.bar(x - bar_width, precision, width=bar_width, label='Precision', color='b')
ax.bar(x, recall, width=bar_width, label='Recall', color='g')
ax.bar(x + bar_width, f1_score, width=bar_width, label='F1-Score', color='r')

ax.set_xlabel('Class Labels')
ax.set_ylabel('Scores')
ax.set_title('Precisão, Recall e F1-Score for SVM')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()
