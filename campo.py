
class Campo:
    
    def __init__(self):
        
        self.coordenadas_de_borrachos = {}
        
        
    def anadir_borracho(self, borracho, coordenada):
        
        self.coordenadas_de_borrachos[borracho] = coordenada
        
    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)
        
        self.coordenadas_de_borrachos[borracho] = nueva_coordenada