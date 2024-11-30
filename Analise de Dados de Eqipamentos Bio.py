import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

dados_oee = {
    'Dia': ['01/01', '02/01', '03/01', '04/01', '05/01', '06/01', '07/01'],
    'Disponibilidade': [0.90, 0.85, 0.95, 0.88, 0.92, 0.91, 0.87],
    'Desempenho': [0.80, 0.75, 0.78, 0.82, 0.79, 0.83, 0.80],
    'Qualidade': [0.95, 0.92, 0.93, 0.91, 0.94, 0.96, 0.90]
}

df_oee = pd.DataFrame(dados_oee)
df_oee['OEE'] = df_oee['Disponibilidade'] * df_oee['Desempenho'] * df_oee['Qualidade']

plt.figure(figsize=(12, 8))
sns.lineplot(x='Dia', y='OEE', data=df_oee, marker='o', color='#1f77b4', linewidth=2.5)
plt.fill_between(df_oee['Dia'], df_oee['OEE'], color='lightblue', alpha=0.3)
plt.title('Eficiência Geral de Equipamentos (OEE)', fontsize=16, fontweight='bold')
plt.ylabel('OEE', fontsize=14)
plt.xlabel('Dia', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.show()

dados_qualidade = {
    'Dia': ['01/01', '02/01', '03/01', '04/01', '05/01', '06/01', '07/01'],
    'Produzidos': [1000, 1200, 1100, 1300, 1150, 1250, 1180],
    'Defeituosos': [50, 60, 40, 70, 55, 65, 62]
}

df_qualidade = pd.DataFrame(dados_qualidade)
df_qualidade['Taxa de Rejeição'] = df_qualidade['Defeituosos'] / df_qualidade['Produzidos']

plt.figure(figsize=(12, 8))
df_qualidade[['Produzidos', 'Defeituosos']].plot(kind='bar', stacked=True, color=['#2ca02c', '#d62728'], edgecolor='black')
plt.title('Produção Total vs Defeituosos', fontsize=16, fontweight='bold')
plt.ylabel('Quantidade', fontsize=14)
plt.xlabel('Dia', fontsize=14)
plt.xticks(rotation=0, fontsize=12)
plt.yticks(fontsize=12)
plt.legend(['Produzidos', 'Defeituosos'], fontsize=12)
plt.grid(True)
plt.show()

dados_manutencao = {
    'Dia': ['01/01', '02/01', '03/01', '04/01', '05/01', '06/01', '07/01'],
    'Falhas Corrigidas': [2, 3, 1, 4, 2, 3, 5],
    'Manutenção Preventiva': [3, 2, 4, 3, 4, 5, 4],
    'Tempo de Inatividade': [5, 8, 3, 10, 6, 7, 8]
}

df_manutencao = pd.DataFrame(dados_manutencao)

plt.figure(figsize=(12, 8))
sns.lineplot(x='Dia', y='Tempo de Inatividade', data=df_manutencao, marker='o', color='#ff7f0e', linewidth=2.5, label='Inatividade')
plt.fill_between(df_manutencao['Dia'], df_manutencao['Tempo de Inatividade'], color='#ffbb78', alpha=0.3)
plt.title('Tempo de Inatividade (Falhas vs Manutenção Preventiva)', fontsize=16, fontweight='bold')
plt.ylabel('Horas de Inatividade', fontsize=14)
plt.xlabel('Dia', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.show(())