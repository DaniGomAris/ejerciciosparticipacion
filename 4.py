#4
class Rectangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def perimetro(self):
    suma = self.base + self.base + self.altura + self.altura
    print(f"El perimetro del rectangulo es: {suma}")


  def area (self):
      area = self.base * self.altura
      print(f"El area del rectangulo es: {area}")

  def es_cuadrado(self):
    print("Es cuadrado?")
    if self.base == self.altura:
      print("Si")
    else:
      print("No")


rectangulo_1 = Rectangulo(4, 5)
rectangulo_1.perimetro()
rectangulo_1.area()
rectangulo_1.es_cuadrado()