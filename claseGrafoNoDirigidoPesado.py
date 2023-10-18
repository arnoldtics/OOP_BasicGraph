#!/usr/bin/env python3
#Author: Arnoldo Fernando Chue Sánchez
#Contact: arnoldwork20@gmail.com
#License: GNU/GPL 

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