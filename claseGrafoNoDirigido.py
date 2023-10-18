#!/usr/bin/env python3
#Author: Arnoldo Fernando Chue Sánchez
#Contact: arnoldwork20@gmail.com
#License: GNU/GPL 

class GrafoNoDirigido:
    def __init__(self):
        self.vertices = set()
        self.aristas = {}
    
    def agregar_vertice(self, vertice):
        self.vertices.add(vertice)
        if vertice not in self.aristas:
            self.aristas[vertice] = set()

    def agregar_arista(self, vertice1, vertice2):
        if vertice1 not in self.vertices:
            self.agregar_vertice(vertice1)
        if vertice2 not in self.vertices:
            self.agregar_vertice(vertice2)
        self.aristas[vertice1].add(vertice2)
        self.aristas[vertice2].add(vertice1)

    def obtener_vertices(self):
        return list(self.vertices)

    def obtener_vecinos(self, vertice):
        if vertice in self.aristas:
            return list(self.aristas[vertice])
        else:
            return []