#!/usr/bin/env python3
#Author: Arnoldo Fernando Chue Sánchez
#Contact: arnoldwork20@gmail.com
#License: GNU/GPL 

import heapq

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.aristas = {}
    
    def agregar_vertice(self, vertice):
        self.vertices.add(vertice)
        if vertice not in self.aristas:
            self.aristas[vertice] = {}

    def agregar_arista(self, vertice1, vertice2, peso):
        if vertice1 not in self.vertices:
            self.agregar_vertice(vertice1)
        if vertice2 not in self.vertices:
            self.agregar_vertice(vertice2)
        self.aristas[vertice1][vertice2] = peso
        self.aristas[vertice2][vertice1] = peso

    def obtener_peso_arista(self, vertice1, vertice2):
        if vertice1 in self.aristas and vertice2 in self.aristas[vertice1]:
            return self.aristas[vertice1][vertice2]
        else:
            return None

    def obtener_vertices(self):
        return list(self.vertices)

    def obtener_vecinos(self, vertice):
        if vertice in self.aristas:
            return list(self.aristas[vertice].keys())
        else:
            return []
        
    def dijkstra(self, inicio):
        distancia = {vertice: float('inf') for vertice in self.vertices}
        distancia[inicio] = 0
        padre = {}

        priority_queue = [(0, inicio)]
        heapq.heapify(priority_queue)

        while priority_queue:
            dist_actual, vertice_actual = heapq.heappop(priority_queue)

            if dist_actual > distancia[vertice_actual]:
                continue

            for vecino in self.obtener_vecinos(vertice_actual):
                peso = self.obtener_peso_arista(vertice_actual, vecino)
                if distancia[vertice_actual] + peso < distancia[vecino]:
                    distancia[vecino] = distancia[vertice_actual] + peso
                    padre[vecino] = vertice_actual
                    heapq.heappush(priority_queue, (distancia[vecino], vecino))

        return distancia, padre