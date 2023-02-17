class Carta:
    Pintas = ("Trebol", "Pica", "Corazon", "Diamante")
    Valores = ("A", "J", "Q", "K", "diez", "nueve", "ocho", "siete", 'seis', 'cinco', 'cuatro', 'tres', 'dos')

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta