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