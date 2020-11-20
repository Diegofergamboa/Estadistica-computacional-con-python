'''
    Implementando algoritmos para hacer una simulacion
    El camino de borrachos es un problema sencillo
    Tres clases: 1) Abstraccion de coordenada
    2) Borracho principal y 3) el Subborracho
'''

[]
import random

class Borracho:
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    
class Borracho_tradicional(Borracho):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
        
    def camina():
        return random.choice([(0,1), (0,-1), (1,0), (-1,0)])
    
    