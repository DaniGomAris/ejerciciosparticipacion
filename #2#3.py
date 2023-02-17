#2 #3
import math

class Punto:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def getx(self):
    return self.x

  def gety(self):
    return self.y

  def mostrar(self):
    print(f"X: {str(self.getx())} \nY: {str(self.gety())}")

  def mover(self, mover_x, mover_y):
    self.x += mover_x
    self.y += mover_y


  def calcular_distancia(self, punto):
    print("La distancia entre los puntos es:")
    return math.sqrt(
        (self.x - punto) ** 2 +
        (self.y - punto) ** 2
                    )

P=Punto(5, 6)
P.mostrar()
P.mover(1, 3)
P.calcular_distancia(2)