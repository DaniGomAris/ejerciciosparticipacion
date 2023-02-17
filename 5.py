#5
class Circulo:
  def __init__(self, centro=5.6, radio=6):
    self.centro = centro
    self.radio = radio

  def area(self):
    print(f"El area es: {3.1416 * (self.radio * self.radio)}")

  def perimetro(self,):
    print(f"El perimetro es: {2 * (3.1416 * self.radio)}")

  def pertenece(self,):
    pass