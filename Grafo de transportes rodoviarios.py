import networkx as nx
import matplotlib.pyplot as plt

# Criando um grafo vazio para representar a rede de transporte rodoviário
G = nx.Graph()

# Adicionando cidades como nós ao grafo com atributos adicionais
cidades = {
    "São Paulo": {"populacao": 12110000},
    "Rio de Janeiro": {"populacao": 6748000},
    "Belo Horizonte": {"populacao": 2524000},
    "Brasília": {"populacao": 3058000},
    "Curitiba": {"populacao": 1933000},
    "Porto Alegre": {"populacao": 1481000},
    "Salvador": {"populacao": 2930000},
    "Fortaleza": {"populacao": 2669000},
    "Recife": {"populacao": 1634000},
    "Manaus": {"populacao": 2217000}
}
G.add_nodes_from(cidades.keys(), **cidades)

# Adicionando estradas como arestas ao grafo com atributos adicionais
estradas = [
    ("São Paulo", "Rio de Janeiro", {"distancia": 430, "tipo_via": "rodovia"}),
    ("São Paulo", "Belo Horizonte", {"distancia": 586, "tipo_via": "rodovia"}),
    ("São Paulo", "Curitiba", {"distancia": 408, "tipo_via": "rodovia"}),
    ("Rio de Janeiro", "Belo Horizonte", {"distancia": 339, "tipo_via": "rodovia"}),
    ("Rio de Janeiro", "Brasília", {"distancia": 1159, "tipo_via": "rodovia"}),
    ("Belo Horizonte", "Brasília", {"distancia": 716, "tipo_via": "rodovia"}),
    ("Belo Horizonte", "Curitiba", {"distancia": 1004, "tipo_via": "rodovia"}),
    ("Belo Horizonte", "Salvador", {"distancia": 1198, "tipo_via": "rodovia"}),
    ("Brasília", "Salvador", {"distancia": 1453, "tipo_via": "rodovia"}),
    ("Salvador", "Recife", {"distancia": 839, "tipo_via": "rodovia"}),
    ("Recife", "Fortaleza", {"distancia": 814, "tipo_via": "rodovia"}),
    ("Fortaleza", "Manaus", {"distancia": 3481, "tipo_via": "rodovia"}),
    ("Manaus", "Porto Alegre", {"distancia": 3282, "tipo_via": "rodovia"}),
    ("Porto Alegre", "Curitiba", {"distancia": 473, "tipo_via": "rodovia"})
]
G.add_edges_from(estradas)

# Visualizando a rede de transporte rodoviário
pos = nx.spring_layout(G)  # posição dos nós
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=8, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d["distancia"] for u, v, d in G.edges(data=True)})
plt.title("Rede de Transporte Rodoviário")
plt.show()

# Exibindo informações adicionais das cidades
print("Informações adicionais das cidades:")
for cidade, atributos in cidades.items():
    print(f"{cidade}: População {atributos['populacao']} habitantes")
