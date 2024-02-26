class Punto:
    def __init__(self, punto_a, punto_b) -> None:
        self.punto_a = punto_a
        self.punto_b = punto_b

    def mostrar(self):
        print(f"La cordenada es {self.punto_a} y {self.punto_b}")

    def mover(self, nueva_coordenada_a,nueva_coordenada_b):
        self.punto_a = nueva_coordenada_a
        self.punto_b = nueva_coordenada_b

    def calcular_distancia(self,):
        pass