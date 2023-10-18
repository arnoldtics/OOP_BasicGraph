#!/usr/bin/env python3
#Author: Arnoldo Fernando Chue Sánchez
#Contact: arnoldwork20@gmail.com
#ICPC useful code
#License: GNU/GPL 

from queue import Queue

class DirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v, capacity):
        self.adj_list[u].append({'v': v, 'capacity': capacity, 'flow': 0})
        self.adj_list[v].append({'v': u, 'capacity': 0, 'flow': 0})

    def max_flow(self, source, sink):
        # Crear una matriz para almacenar las capacidades residuales
        residual_graph = [[edge['capacity'] for edge in self.adj_list[vertex]] for vertex in range(self.num_vertices)]

        # Inicializar el flujo máximo en 0
        max_flow = 0

        # Repetir mientras exista un camino aumentante desde la fuente hasta el sumidero
        while self.bfs(source, sink, residual_graph):
            # Encontrar el flujo máximo que se puede enviar a lo largo del camino aumentante
            path_flow = float('inf')
            v = sink
            while v != source:
                u = self.parent[v]
                for edge in self.adj_list[u]:
                    if edge['v'] == v:
                        path_flow = min(path_flow, residual_graph[u][edge_index])
                        break
                v = u

            # Actualizar las capacidades residuales y los flujos a lo largo del camino aumentante
            v = sink
            while v != source:
                u = self.parent[v]
                for edge_index, edge in enumerate(self.adj_list[u]):
                    if edge['v'] == v:
                        residual_graph[u][edge_index] -= path_flow
                        residual_graph[v][edge['v']] += path_flow
                        edge['flow'] += path_flow
                        break
                v = u

            # Aumentar el flujo máximo
            max_flow += path_flow

        return max_flow

    def bfs(self, source, sink, residual_graph):
        # Inicializar los nodos visitados y la cola para el BFS
        visited = [False] * self.num_vertices
        self.parent = [-1] * self.num_vertices
        queue = Queue()

        # Marcar la fuente como visitada y agregarla a la cola
        visited[source] = True
        queue.put(source)

        # Búsqueda BFS
        while not queue.empty():
            u = queue.get()

            for edge_index, edge in enumerate(self.adj_list[u]):
                v = edge['v']
                capacity = residual_graph[u][edge_index]

                if not visited[v] and capacity > 0:
                    visited[v] = True
                    self.parent[v] = u
                    queue.put(v)

        # Si se alcanzó el sumidero durante la búsqueda, hay un camino aumentante
        return visited[sink]
