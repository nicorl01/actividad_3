class Vehiculo:
    def __init__(self, velocidad_maxima,kilometraje) -> None:
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

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


class Circulo:
    def __init__(self, centro , radio) -> None:
        self.centro = centro
        self.radio = radio
    

class Carta:    

    CORAZON = "â™¥"
    DIAMANTE = "â™¦"
    TREBOL = "â™£"
    PICA = "â™ "

    def __init__(self, valor,pinta) -> None:
        self.valor = valor
        self.pinta = pinta

    def imprimir(self):
        print(self.valor, self.pinta)    

# a = Carta(10, Carta.CORAZON) 
# a.imprimir()       


class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios,balance) -> None:
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, valor_deposito):
        self.balance += valor_deposito

    def retirar(self, valor_retirar):
        if self.balance < valor_retirar:
            print("No tiene la cantidad suficiente")
        else:
            self.balance += valor_retirar

    def aplicar_cupota_manejo(self):
        print(self.balance * 0.2)

    def mostrar_detalle(self):
        print(f"{self.balance}, {self.numero_cuenta}, {self.propietarios}")                  

# r1 = Rectangulo([1,3], [3,1])
# r1.calcular_area()      
# r1.calcular_perimetro()     
# r1.cuadrado() 