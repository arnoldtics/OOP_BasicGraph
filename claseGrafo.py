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
    