class CalcularSueldo:

    def __init__(self, sueldoBasico, horasExtras, diasFalta, minutosTardanza):
        self.sueldoBasico = sueldoBasico
        self.horasExtras = horasExtras
        self.diasFalta = diasFalta
        self.minutosTardanza = minutosTardanza


    def calculoBonificaciones(self):


        # Bonificación por horas extras (50% más que una hora normal)
        pagoHorasExtras = 1.50 * self.horasExtras * self.sueldoBasico / 30 / 8

        # Bonificación por movilidad (1000)
        bonificacionMovilidad = 1000

        # Bonificación suplementaria (3% del sueldo básico)
        bonificacionSuplementaria = 0.03 * self.sueldoBasico

        # bonificacion total
        bonificaciones = bonificacionMovilidad + bonificacionSuplementaria + pagoHorasExtras
        return bonificaciones

    def calculoDescuento(self):
        #remuneracion computable = sueldoBasico + movilidad (1000) + bonificacionSuplementaria
        remuneracionComputable = self.sueldoBasico + 1000 + (0.03 * self.sueldoBasico)

        # Descuento por faltas
        descuentoFaltas = (remuneracionComputable / 30) * self.diasFalta

        # Descuento por tardanzas
        descuentoTardanzas = (((remuneracionComputable / 30) / 8) / 60) * self.minutosTardanza

        descuentos = descuentoFaltas + descuentoTardanzas
        return descuentos

    def calculoSueldoNeto(self):
        bonificaciones = self.calculoBonificaciones()
        descuentos = self.calculoDescuento()

        # calcula sueldo neto
        sueldoNeto = self.sueldoBasico + bonificaciones - descuentos
        return sueldoNeto

    def remuneracionMinima(self):
        # remuneracion minima
        remuneracionMinima = self.sueldoBasico + self.calculoBonificaciones()
        return remuneracionMinima
