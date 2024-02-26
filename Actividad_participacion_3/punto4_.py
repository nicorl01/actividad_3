class Rectangulo:
    def __init__(self,esquina_1, esquina_2 ) -> None:
        self.esquina_1 = esquina_1
        self.esquina_2 = esquina_2

    def calcular_area(self):
        lado1 = self.esquina_2[0] - self.esquina_1[0]
        lado2 = self.esquina_1[1] - self.esquina_2[1]

        print(lado1 * lado2) 
    
    def calcular_perimetro(self):
        lado1 = self.esquina_2[0] - self.esquina_1[0]
        lado2 = self.esquina_1[1] - self.esquina_2[1]

        print(lado1 + lado1 + lado2 + lado2)

    def cuadrado(self):
        lado1 = self.esquina_2[0] - self.esquina_1[0]
        lado2 = self.esquina_1[1] - self.esquina_2[1]
        if lado1 == lado2:
            print("Es un cudrado")

        else:
            print("No es un cuadrado")