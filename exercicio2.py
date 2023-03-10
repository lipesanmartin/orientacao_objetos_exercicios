class Quadrado:
    def __init__(self, side):
        self.lado = side
        print("O lado do quadrado é", self.lado)

    def mudar_lado(self):
        self.lado = int(input("Insira o novo lado do quadrado: "))

    def retornar_lado(self):
        print("O lado do quadrado agora é", self.lado)

    def calcular_area(self):
        area = self.lado * self.lado
        print(f"A área do quadrado de lado {self.lado} é {area}.")


lado = int(input("Insira o lado do quadrado: "))

quadrado = Quadrado(lado)
quadrado.mudar_lado()
quadrado.retornar_lado()
quadrado.calcular_area()
