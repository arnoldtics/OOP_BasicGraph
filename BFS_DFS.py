#!/usr/bin/env python3
#Author: Arnoldo Fernando Chue Sánchez
#Contact: arnoldwork20@gmail.com
#License: GNU/GPL 

from collections import deque

class Grafo:
    def __init__(self, n):
        self.n = [set() for i in range(n)]
    
    def agregar_arista(self, u, v):
        self.n[u].add(v) 
        self.n[v].add(u)
    
    def quitar_arista(self, u, v):
        self.n[u].remove(v)
        self.n[v].remove(u)
    
    def vecinos(self, u):
        return self.n[u]
    
    def son_vecinos(self, u, v):
        return u in self.n[v]
    
    def bfs_completo(self, inicio):
        visitado = [False] * len(self.n)
        distancia = [float('inf')] * len(self.n)
        padre = [-1] * len(self.n)

        visitado[inicio] = True
        distancia[inicio] = 0

        queue = deque()
        queue.append(inicio)

        while queue:
            u = queue.popleft()

            for v in self.vecinos(u):
                if not visitado[v]:
                    visitado[v] = True
                    distancia[v] = distancia[u] + 1
                    padre[v] = u
                    queue.append(v)

        return distancia, padre
    
    def bfs_inicio_objetivo(self, inicio, objetivo):
        visitado = [False] * len(self.n)
        distancia = [float('inf')] * len(self.n)
        padre = [-1] * len(self.n)

        visitado[inicio] = True
        distancia[inicio] = 0

        queue = deque()
        queue.append(inicio)

        while queue:
            u = queue.popleft()

            if u == objetivo:
                break

            for v in self.vecinos(u):
                if not visitado[v]:
                    visitado[v] = True
                    distancia[v] = distancia[u] + 1
                    padre[v] = u
                    queue.append(v)

        if distancia[objetivo] == float('inf'):
            return -1  # No se encontró un camino al objetivo
        else:
            return distancia[objetivo]
        
    def dfs_completo(self, inicio):
        visitado = [False] * len(self.n)
        distancia = [float('inf')] * len(self.n)
        padre = [-1] * len(self.n)

        visitado[inicio] = True
        distancia[inicio] = 0

        stack = deque()
        stack.append(inicio)

        while stack:
            u = stack.pop()

            for v in self.vecinos(u):
                if not visitado[v]:
                    visitado[v] = True
                    distancia[v] = distancia[u] + 1
                    padre[v] = u
                    stack.append(v)

        return distancia, padre
    
    def dfs_inicio_objetivo(self, inicio, objetivo):
        visitado = [False] * len(self.n)
        distancia = [float('inf')] * len(self.n)
        padre = [-1] * len(self.n)

        visitado[inicio] = True
        distancia[inicio] = 0

        stack = deque()
        stack.append(inicio)

        while stack:
            u = stack.pop()

            if u == objetivo:
                break

            for v in self.vecinos(u):
                if not visitado[v]:
                    visitado[v] = True
                    distancia[v] = distancia[u] + 1
                    padre[v] = u
                    stack.append(v)

        if distancia[objetivo] == float('inf'):
            return -1  # No se encontró un camino al objetivo
        else:
            return distancia[objetivo]