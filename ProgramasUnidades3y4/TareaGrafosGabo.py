import networkx as nx

class SemaforoGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

        # Agregar estados al grafo
        estados = ["ESTADO ROJO", "ESTADO VERDE", "VERDE PARPADEO", "AMARILLO PARPADEO", "ESTADO AMARILLO"]
        self.graph.add_nodes_from(estados)

        # Definir las relaciones entre los estados
        relaciones = [
            ("ESTADO ROJO", "AMARILLO PARPADEO"),
            ("ESTADO ROJO", "ESTADO AMARILLO"),
            ("ESTADO VERDE", "ESTADO ROJO"),
            ("VERDE PARPADEO", "AMARILLO PARPADEO"),
            ("AMARILLO PARPADEO", "ESTADO ROJO"),
            ("AMARILLO PARPADEO", "VERDE PARPADEO"),
            ("AMARILLO PARPADEO", "ESTADO VERDE"),
            ("AMARILLO PARPADEO", "ESTADO AMARILLO"),
            ("ESTADO AMARILLO", "VERDE PARPADEO"),
        ]

        # Agregar relaciones al grafo
        self.graph.add_edges_from(relaciones)

    def imprimir_relaciones(self):
        for estado in self.graph.nodes:
            vecinos = list(self.graph.neighbors(estado))
            print(f"Los estados conectados a '{estado}' son: {vecinos}")

def main():
    semaforo = SemaforoGraph()
    semaforo.imprimir_relaciones()

if __name__ == '__main__':
    main()
