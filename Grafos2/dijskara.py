from queue import PriorityQueue

class Grafo:
    def __init__(self, numero_de_vertices):
        self.v = numero_de_vertices
        self.edges = [[-1 for i in range(numero_de_vertices)] for j in range(numero_de_vertices)]
        self.visited = []

    def add_arestas(self, u, v, weight):
        self.arestas[u][v] = weight
        self.arestas[v][u] = weight

    def dijkstra(grafo, vertice):
        D = {v:float('inf') for v in range(grafo.v)}
        D[vertice] = 0

        pq = PriorityQueue()
        pq.put((0, vertice))

        while not pq.empty():
            (dist, vertice) = pq.get()
            grafo.visitado.append(vertice)

            for vizinho in range(grafo.v):
                if grafo.edges[vertice][vizinho] != -1:
                    distancia = grafo.edges[vertice][vizinho]
                    if vizinho not in grafo.visitado:
                        old_cost = D[vizinho]
                        new_cost = D[vertice] + distancia
                        if new_cost < old_cost:
                            pq.put((new_cost, vizinho))
                            D[vizinho] = new_cost
        return D