import matplotlib.pyplot as plt
import numpy as np

# Definindo as tensões e parâmetros do conversor
tensao_ac = 220  # Tensão AC em volts
tensao_dc = 12   # Tensão DC em volts
eficiencia = 0.85  # Eficiência do conversor (85%)

# Potência nominal da carga
potencia_carga_watts = 24  # Watts

# Corrente na carga DC
corrente_dc = potencia_carga_watts / tensao_dc

# Corrente na entrada AC, considerando eficiência
potencia_entrada = potencia_carga_watts / eficiencia
corrente_ac = potencia_entrada / tensao_ac

# Dados para o gráfico de barras
etiquetas = ['Entrada AC (220V)', 'Saída DC (12V)']
valores = [tensao_ac, tensao_dc]

# Criar o gráfico de tensões
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(etiquetas, valores, color=['blue', 'green'])
plt.xlabel('Tipo de Tensão')
plt.ylabel('Tensão (V)')
plt.title('Conversão de Tensão AC para DC')
plt.ylim(0, max(valores) + 50)  # Ajustar o limite do eixo y para melhor visualização

for i, valor in enumerate(valores):
    plt.text(i, valor + 5, f'{valor}V', ha='center')


resistencias = np.linspace(1, 10, 100)  # Resistências de 1 a 10 ohms
corrente = tensao_dc / resistencias  # Corrente DC para diferentes resistências

plt.subplot(1, 2, 2)
plt.plot(resistencias, corrente, color='red')
plt.xlabel('Resistência (Ω)')
plt.ylabel('Corrente DC (A)')
plt.title('Corrente DC vs. Resistência')
plt.grid(True)

for i, valor in enumerate(resistencias[::10]):
    plt.text(resistencias[::10][i], corrente[::10][i], f'{corrente[::10][i]:.2f}A', ha='right')

plt.tight_layout()
plt.show()

print(f'Corrente DC necessária: {corrente_dc:.2f} A')
print(f'Corrente AC consumida: {corrente_ac:.2f} A (considerando eficiência de {eficiencia*100:.0f}%)')
