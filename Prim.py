#!/usr/bin/env python3
#Author: Arnoldo Fernando Chue Sánchez
#Contact: arnoldwork20@gmail.com
#License: GNU/GPL 

import heapq

class Grafo:
    def __init__(self, n):
        self.V = [[] for _ in range(n)]
        self.W = {}
        
    def vecinos(self, u):
        return self.V[u]
    
    def agregar_arista(self, u, v, w = 1):
        self.V[u].append(v)
        self.V[v].append(u)
        
        self.W[(u,v)] = w
    
    def peso(self, u, v):
        if (u,v) in self.W: 
            return self.W[(u,v)]
        return self.W[(v,u)]
    
class cola_de_prioridad:
    def __init__(self, H = []):
        self.H = H
        heapq.heapify(self.H)
        
    def dame_la_mas_chiquita_y_quitala(self):
        return heapq.heappop(self.H)
    
    def agrega(self, s):
        heapq.heappush(self.H, s)
        
    def no_esta_vacia(self):
        return self.H
    
def prim(G:Grafo):
    vertices_explorados = {0}
    
    aristas_por_explorar = cola_de_prioridad([(G.peso(0,v),0,v) for v in G.vecinos(0)])
    
    arbol = []
    while aristas_por_explorar.no_esta_vacia():
        s = aristas_por_explorar.dame_la_mas_chiquita_y_quitala()
        w, u, v = s 
        if v not in vertices_explorados:
            arbol.append(s)
            if len(arbol) == len(G.V)-1: return arbol
            vertices_explorados.add(v)
            for a in G.vecinos(v):
                if a not in vertices_explorados:
                    peso = G.peso(a, v)
                    aristas_por_explorar.agrega((peso,v,a))
    return arbol