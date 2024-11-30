import matplotlib.pyplot as plt
import numpy as np

# Dados
metrics = ['Precisão', 'Sensibilidade', 'Especificidade', 'Falsos Positivos']
svm_values = [94, 92, 96, 4]
traditional_values = [85, 80, 83, 10]

# Configurações de estilo
plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Largura das barras
bar_width = 0.35
index = np.arange(len(metrics))

# Barras
bar1 = ax.bar(index, svm_values, bar_width, label='SVM', color='royalblue', edgecolor='black')
bar2 = ax.bar(index + bar_width, traditional_values, bar_width, label='Métodos Tradicionais', color='orange', edgecolor='black')

# Adicionar rótulos e títulos
ax.set_xlabel('Métricas', fontsize=14, fontweight='bold')
ax.set_ylabel('Percentual (%)', fontsize=14, fontweight='bold')
ax.set_title('Comparação de Desempenho: SVM vs Métodos Tradicionais', fontsize=16, fontweight='bold')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(metrics, fontsize=12)
ax.legend()

# Adicionar rótulos de valor nas barras
for bar in bar1:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, f'{yval}%', ha='center', va='bottom', fontsize=12, fontweight='bold')
for bar in bar2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, f'{yval}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Mostrar gráfico
plt.tight_layout()
plt.show()
