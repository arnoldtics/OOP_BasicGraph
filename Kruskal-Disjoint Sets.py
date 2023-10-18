#!/usr/bin/env python3
#Author: Arnoldo Fernando Chue Sánchez
#Contact: arnoldwork20@gmail.com
#License: GNU/GPL 

import random 

rr = random.randrange

# Aquí vamos a usar una representación distinta de lo habitual para el grafo
n = 10 # número de vértices
# Los vértices están numerados del 0 a n-1
m = 40 # número de aristas

# Las aristas se componen por (u,v,w), donde u y v son los vértices que
# une la arista y w es el peso
E = [(rr(0,n), rr(0,n), rr(0,1000)) for _ in range(m)]
E = [(u,v,w) for u,v,w in E if u != v]

# Función para manejar el peso de nuestro grafo de acuerdo a nuestra representación
def peso(e): return e[2]

# Primero usamos nuestra clase de Disjoint Sets
class DisjointSets:
    def __init__(self, n):
        self.p = [None for _ in range(n)] # padres
        
    def raiz(self, u):
        if self.p[u] is None: return u
        r = self.raiz(self.p[u])
        self.p[u] = r # compresión de caminos
        return r
        
    def juntar(self, u, v):
        ru, rv = self.raiz(u), self.raiz(v)
        if ru != rv:
            self.p[ru] = rv
    
    def misma_componente(self, u, v): return self.raiz(u) == self.raiz(v)

# Ahora sí programamos Kruskal
def kruskal(E, n):
    E.sort(key=peso)
    A = []
    D = DisjointSets(n)
    for e in E:
        if len(A) == 0: A.append(e)
        if not D.misma_componente(e, A[0]):
            A.append(e)
            if len(A) == n-1: return A
            D.juntar(A[0], e)
    return A