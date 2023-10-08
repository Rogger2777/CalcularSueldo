class ImprimirBoleta:
    def __init__(self, sueldoBasico, bonificaciones, descuento, sueldoNeto, renumeracionMinima):
        self.sueldoBasico = sueldoBasico
        self.bonificaciones = bonificaciones
        self.descuento = descuento
        self.sueldoNeto = sueldoNeto
        self.renumeracionMinima = renumeracionMinima

    def ImprimirResultados(self):
        print("========BOLETA DE PAGO=========")
        print(f"Sueldo Basico:       {self.sueldoBasico}")
        print(f"Bonificaciones:      {self.bonificaciones}")
        print(f"Descuentos:          {self.descuento}")
        print(f"Remuneracion Minima: {self.renumeracionMinima}")
        print(f"Sueldo Neto:         {self.sueldoNeto}")
