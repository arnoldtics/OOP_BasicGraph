#!/usr/bin/env python3
#Author: Arnoldo Fernando Chue Sánchez
#Contact: arnoldwork20@gmail.com
#License: GNU/GPL 

class GrafoDirigido:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = {}

    def agregar_arista(self, origen, destino, peso=1):
        if origen in self.grafo and destino in self.grafo:
            self.grafo[origen][destino] = peso

    def obtener_vertices(self):
        return list(self.grafo.keys())

    def obtener_aristas(self):
        aristas = []
        for origen in self.grafo:
            for destino in self.grafo[origen]:
                aristas.append((origen, destino, self.grafo[origen][destino]))
        return aristas

    def obtener_vecinos(self, vertice):
        if vertice in self.grafo:
            return list(self.grafo[vertice].keys())
        return []

    def obtener_peso_arista(self, origen, destino):
        if origen in self.grafo and destino in self.grafo[origen]:
            return self.grafo[origen][destino]
        return None

    def eliminar_arista(self, origen, destino):
        if origen in self.grafo and destino in self.grafo[origen]:
            del self.grafo[origen][destino]

    def eliminar_vertice(self, vertice):
        if vertice in self.grafo:
            del self.grafo[vertice]
            for vertices in self.grafo.values():
                if vertice in vertices:
                    del vertices[vertice]
