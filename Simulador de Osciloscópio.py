import numpy as np
import matplotlib.pyplot as plt

frequencia = 50
amplitude_entrada = 220 * np.sqrt(2)
amplitude_saida = 12 * np.sqrt(2)
tempo = np.linspace(0, 0.1, 1000)
carga_resistencia = 100
capacitancia = 1000e-6

tensao_entrada = amplitude_entrada * np.sin(2 * np.pi * frequencia * tempo)
tensao_transformada = amplitude_saida * np.sin(2 * np.pi * frequencia * tempo)
tensao_retificada = np.abs(tensao_transformada)
tensao_filtrada = amplitude_saida - (amplitude_saida - tensao_retificada) * np.exp(-tempo / (carga_resistencia * capacitancia))
tensao_regulada = np.full_like(tempo, 12)

plt.figure(figsize=(14, 10))

plt.subplot(5, 1, 1)
plt.plot(tempo, tensao_entrada, label='Tensão AC (220V)', color='blue')
plt.title('Tensão de Entrada (220V AC)')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.legend()

plt.subplot(5, 1, 2)
plt.plot(tempo, tensao_transformada, label='Tensão Após Transformador (12V AC)', color='orange')
plt.title('Tensão Após Transformador (12V AC)')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.legend()

plt.subplot(5, 1, 3)
plt.plot(tempo, tensao_retificada, label='Tensão Retificada (DC Pulsante)', color='red')
plt.title('Tensão Após Retificação (Onda Completa)')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.legend()

plt.subplot(5, 1, 4)
plt.plot(tempo, tensao_filtrada, label='Tensão Após Filtro Capacitivo', color='green')
plt.title('Tensão Após Filtro Capacitivo')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.legend()

plt.subplot(5, 1, 5)
plt.plot(tempo, tensao_regulada, label='Tensão Após Regulador (12V DC)', color='purple')
plt.title('Tensão Após Regulador de Tensão')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
