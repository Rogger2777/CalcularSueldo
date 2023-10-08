class CalcularSueldo:

    def __init__(self, sueldoBasico, horasExtras, ):
        self.sueldoBasico = sueldoBasico
        self.horasExtras = horasExtras

    def calculoBonificaciones(self):
        # Bonificación por horas extras (50% más que una hora normal)
        horaNormal = (self.sueldoBasico/30)/8
        bonificacionHoraExtra = 1.5 * self.horasExtras * self.sueldoBasico / (30 / 8)

        # Bonificación por movilidad (1000)
        bonificacionMovilidad = 1000

        # Bonificación suplementaria (3% del sueldo básico)
        bonificacionSuplementaria = 0.03 * self.sueldoBasico

        bonificaciones = bonificacionHoraExtra + bonificacionMovilidad + bonificacionSuplementaria
        return bonificaciones

    def calculoDescuento(self, descuentos):
        # Aquí puedes calcular los descuentos si es necesario
        return descuentos

    def calculoSueldoNeto(self):
        bonificaciones = self.calculoBonificaciones()
        descuentos = self.calculoDescuento(0)  # Puedes agregar descuentos si es necesario

        sueldoNeto = self.sueldoBasico + bonificaciones - descuentos
        return sueldoNeto
