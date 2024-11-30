import networkx as nx
import matplotlib.pyplot as plt
import heapq


def astar(graph, start, goal):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (0, start))

    # Dicionários para armazenar o custo total estimado do nó inicial ao nó atual (g) e do nó atual ao nó objetivo (h)
    g = {node: float('inf') for node in graph.nodes()}
    h = {node: nx.shortest_path_length(graph, node, goal) for node in graph.nodes()}
    g[start] = 0

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = []
            while current_node != start:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1]

        closed_list.add(current_node)

        for neighbor in graph.neighbors(current_node):
            if neighbor in closed_list:
                continue

            tentative_g = g[current_node] + 1  # assumindo arestas não ponderadas

            if tentative_g < g[neighbor]:
                came_from[neighbor] = current_node
                g[neighbor] = tentative_g
                f = tentative_g + h[neighbor]
                heapq.heappush(open_list, (f, neighbor))

    return None


# Criar um grafo representando a rede social
G = nx.Graph()

# Adicionar nós (usuários)
users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
G.add_nodes_from(users)

# Adicionar arestas (conexões de amizade)
connections = [('Alice', 'Bob'), ('Alice', 'Charlie'), ('Alice', 'David'),
               ('Bob', 'Charlie'), ('Bob', 'David'), ('Charlie', 'David'),
               ('David', 'Eve')]
G.add_edges_from(connections)

# Calcular métricas de centralidade
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
clustering_coefficient = nx.clustering(G)

# Visualizar o grafo
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G)
node_color = [degree_centrality[node] for node in G.nodes()]
nodes = nx.draw_networkx_nodes(G, pos, node_color=node_color, cmap=plt.cm.Blues, node_size=1500)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_color='black', font_size=12, font_weight='bold')

# Adicionar barra de cores
cbar = plt.colorbar(nodes, label='Grau de Centralidade')

plt.title('Rede Social')
plt.show()

# Identificar comunidades na rede
communities = nx.algorithms.community.greedy_modularity_communities(G)
print("Comunidades na rede:")
for i, community in enumerate(communities):
    print(f"Comunidade {i + 1}: {list(community)}")

# Identificar usuários mais influentes
print("\nUsuários mais influentes:")
top_influential_users = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:3]
for user in top_influential_users:
    print(f"{user}: Degree Centrality = {degree_centrality[user]}, "
          f"Betweenness Centrality = {betweenness_centrality[user]}, "
          f"Closeness Centrality = {closeness_centrality[user]}")

# Exibir outras métricas
print("\nMétricas adicionais:")
for user in users:
    print(f"{user}: Clustering Coefficient = {clustering_coefficient[user]}")

# Identificar o caminho mais curto entre dois usuários usando A*
start_node = 'Alice'
goal_node = 'Eve'

shortest_path = astar(G, start_node, goal_node)
if shortest_path:
    print(f"\nCaminho mais curto de {start_node} para {goal_node}: {shortest_path}")
    print(f"Comprimento do caminho: {len(shortest_path) - 1}")
else:
    print(f"\nNão há caminho de {start_node} para {goal_node}.")
