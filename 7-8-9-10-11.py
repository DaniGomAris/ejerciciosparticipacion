class CuentaBancaria:
    def __init__(self, numero_cuenta: int, propietarios: str,  balance: int):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def Depositar(self, valor: int):
        self.balance += valor

    def Retirar(self, valor: int):
        self.balance -= valor

    def Aplicar_cuota_manejo(self, porcentaje=0.02):
        tarifa = porcentaje * self.balance
        self.balance += tarifa

    def Mostrar_detalles(self):
        print(f"los detalles de su cuenta son los siguientes ,\n"
              f"su numero de cuenta es: {self.numero_cuenta},\n"
              f"los propietarios de dicha cuenta son: {self.propietarios},\n"
              f"el balance total de la cuenta antes de la cuota de manejo es: {self.balance},\n"
              f"despues de la cuota seria { self.Aplicar_cuota_manejo() }")