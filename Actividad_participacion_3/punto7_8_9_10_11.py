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