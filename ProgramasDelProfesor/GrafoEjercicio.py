import networkx as nx
"""Se importa a la clase ListaEnlazada para almacenar los nombres de los actores"""
from Lista import ListaEnlazada
class Grafo:
    def __init__(self):
        """En el constructor se crea el grafo y se agregan los valores de los
        atributos de los nodos y de las aristas
        """
        self.grafo=nx.Graph()
        """Se crea una lista enlazada y se agregan los nombres de los actores (aun faltan 
        nombres de actores por agregar).
        Se va a emplear para luego obtener automaticamente (mediante un ciclo for o while)
        las aristas y los nodos vecinos de cada uno en el grafo"""
        self.lista_enlazada=ListaEnlazada()
        self.lista_enlazada.AgregarUltimo("Kevin Bacon")


        """Se agregan los nodos"""
        self.grafo.add_node("Kevin Bacon")
        self.grafo.add_nodes_from(["Tom Hanks", "Meg Ryan", "Parker Posey", "Lisa Kudrow"])
        """Se agregan las aristas"""
        self.grafo.add_edge("Kevin Bacon", "Tom Hanks")
        self.grafo.add_edges_from([("Kevin Bacon", "Meg Ryan"), 
                      ("Tom Hanks", "Meg Ryan"), 
                      ("Tom Hanks", "Parker Posey"), 
                      ("Parker Posey", "Meg Ryan"),
                      ("Parker Posey", "Lisa Kudrow")])
        
        """Se agregan los atributos de las aristas"""
        self. grafo.edges["Kevin Bacon", "Meg Ryan"]["pelicula"]="En carne viva"
        self.grafo.edges["Kevin Bacon", "Tom Hanks"]["pelicula"]="Apolo 13"
        self.grafo.edges["Tom Hanks", "Meg Ryan"]["pelicula"]="Una pelicula"
        self.grafo.edges["Tom Hanks", "Parker Posey"]["pelicula"]="Tienes un email"
        self.grafo.edges["Parker Posey", "Meg Ryan"]["pelicula"]="Algo para recordar"
        self.grafo.edges["Parker Posey", "Lisa Kudrow"]["pelicula"]="Esperando la hora"
        
        """Se agregan los atributos de los nodos"""
        self.grafo.nodes["Kevin Bacon"]["Estudio_cine"]="Marvel"
        self.grafo.nodes["Meg Ryan"]["Estudio_cine"]="Universal"
        self.grafo.nodes["Parker Posey"]["Estudio_cine"]="Leon"
        self.grafo.nodes["Lisa Kudrow"]["Estudio_cine"]="Century"
        self.grafo.nodes["Tom Hanks"]["Estudio_cine"]="Warner"
        
    def imprimir_nodos(self):
        """Se imprimen los atributos de los nodos"""
        print("Nodos:\n",self.grafo.nodes(data=True))
    
    def imprimir_aristas(self):
        """Se imprimen los atributos de las aristas"""
        print("Aristas:\n",self.grafo.edges(data=True))
    
    """El metodo imprimir_vecinos se va a emplear para mostrar los nodos vecinos
    de todos aquellos nodos que conforman el grafo (Kevin Bacon, Tom Hanks, Meg Ryan, Parker Posey, Lisa Kudrow)
    tomando en cuenta que faltan nombres por agregar a la lista"""    
    def imprimir_vecinos(self):
        for i in range(self.lista_enlazada.Tamanio()):
            print("Los nodos vecinos de",self.lista_enlazada.GetNodo(i),"son: ",(list(self.grafo.neighbors(self.lista_enlazada.GetNodo(i)))))
    
    """De la misma forma que el metodo imprimir_vecinos, se debe crear un ciclo for o while
    para recorrer la lista y obtener las aristas de cada nodo del grafo"""
    def imprimir_aristas_de_cada_nodo(self):
        """Ejemplo de como obtener la arista con su atributo del nodo Kevin Bacon.
        Hace falta que se impriman las aristas de todos los nodos mediante un ciclo y 
        la lista enlazada"""
        print("Las aristas (con su atributo pelicula) de Kevin Bacon son: ",(list(self.grafo.edges("Kevin Bacon", data=True))))
        
"""El metodo main crea el objeto de tipo Grafo y llama a los metodos para imprimir
los valores de los atributos de los nodos y las aristas"""
def main():
    g=Grafo()
    # g.imprimir_nodos()
    # g.imprimir_aristas()
    g.imprimir_vecinos()
    """Se imprimen las aristas de cada nodo"""
    g.imprimir_aristas_de_cada_nodo()

if __name__=='__main__':
    main()
"""Importante: para crear un grafo dirigido se llama a la clase DiGraph de networkx
por ejemplo:
grafo_dirigido=nx.DiGraph() 
y posteriormente se emplean los metodos add_node(), add_nodes_from(), edges[], y nodes[] 
para agregar los nodos y aristas del grafo"""