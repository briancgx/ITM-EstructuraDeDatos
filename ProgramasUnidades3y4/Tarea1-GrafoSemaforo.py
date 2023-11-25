# Brian Azael Cumi Guzman 3SA

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_node("ROJO", estado="rojo")
G.add_node("VERDE", estado="verde")
G.add_node("VERDE PARPADEO", estado="verde parpadeo")
G.add_node("AMARILLO PARPADEO", estado="amarillo parpadeo")
G.add_node("AMARILLO", estado="amarillo")

G.add_edge("VERDE PARPADEO", "AMARILLO", relacion="apunta a")
G.add_edge("VERDE PARPADEO", "AMARILLO PARPADEO", relacion="apunta a")  # Relación adicional
G.add_edge("AMARILLO", "AMARILLO PARPADEO", relacion="apunta a")
G.add_edge("VERDE", "AMARILLO PARPADEO", relacion="apunta a")
G.add_edge("ROJO", "AMARILLO PARPADEO", relacion="apunta a")
G.add_edge("VERDE", "VERDE PARPADEO", relacion="apunta a")
G.add_edge("ROJO", "VERDE", relacion="apunta a")
G.add_edge("AMARILLO PARPADEO", "ROJO", relacion="apunta a")
G.add_edge("AMARILLO", "ROJO", relacion="apunta a")

node_colors = {
    "rojo": "red",
    "verde": "green",
    "verde parpadeo": "lightgreen",
    "amarillo parpadeo": "yellow",
    "amarillo": "yellow"
}

node_colors = [node_colors[G.nodes[node]['estado']] for node in G.nodes]

for node in G.nodes:
    print(f"Nodo: {node}, Estado: {G.nodes[node]['estado']}")

for edge in G.edges:
    source_node = G.nodes[edge[0]]['estado']
    target_node = G.nodes[edge[1]]['estado']
    relacion = G[edge[0]][edge[1]]['relacion']
    print(f"Arista: {source_node} apunta a {target_node}")


# Esta parte la hice dibujar el grafo porque se ve bonito, pero al ser innecesaria la comenté en el trabajo.
'''
pos = nx.spring_layout(G, seed=42) 
nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, font_color='black')
edge_labels = nx.get_edge_attributes(G, 'relacion')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
'''