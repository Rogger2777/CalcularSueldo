
import unittest
from src.CalculoSueldoPagar import CalcularSueldo

class TestCalcularSueldo(unittest.TestCase):
    def test_calculoBonificaciones(self):
        # Prueba con valores específicos
        sueldoBasico = 2000
        horasExtras = 10
        diasFalta = 2
        minutosTardanza = 30

        calcular = CalcularSueldo(sueldoBasico, horasExtras, diasFalta, minutosTardanza)
        resultado = calcular.calculoBonificaciones()

        # Calcula el valor esperado manualmente
        bonificacionMovilidad = 1000
        bonificacionSuplementaria = 0.03 * sueldoBasico
        pagoHorasExtras = 1.50 * horasExtras * sueldoBasico / 30 / 8
        valor_esperado = bonificacionMovilidad + bonificacionSuplementaria + pagoHorasExtras

        self.assertEqual(resultado, valor_esperado)

    def test_calculoDescuento(self):
        # Prueba con valores específicos
        sueldoBasico = 2000
        horasExtras = 10
        diasFalta = 2
        minutosTardanza = 30

        calcular = CalcularSueldo(sueldoBasico, horasExtras, diasFalta, minutosTardanza)
        resultado = calcular.calculoDescuento()

        # Calcula el valor esperado manualmente
        remuneracionComputable = sueldoBasico + 1000 + (0.03 * sueldoBasico)
        descuentoFaltas = (remuneracionComputable / 30) * diasFalta
        descuentoTardanzas = (((remuneracionComputable / 30) / 8) / 60) * minutosTardanza
        valor_esperado = descuentoFaltas + descuentoTardanzas

        self.assertEqual(resultado, valor_esperado)

    def test_calculoSueldoNeto(self):
        # Prueba con valores específicos
        sueldoBasico = 2000
        horasExtras = 10
        diasFalta = 2
        minutosTardanza = 30

        calcular = CalcularSueldo(sueldoBasico, horasExtras, diasFalta, minutosTardanza)
        resultado = calcular.calculoSueldoNeto()

        # Calcula el valor esperado manualmente
        bonificacionMovilidad = 1000
        bonificacionSuplementaria = 0.03 * sueldoBasico
        pagoHorasExtras = 1.50 * horasExtras * sueldoBasico / 30 / 8
        remuneracionComputable = sueldoBasico + 1000 + (0.03 * sueldoBasico)
        descuentoFaltas = (remuneracionComputable / 30) * diasFalta
        descuentoTardanzas = (((remuneracionComputable / 30) / 8) / 60) * minutosTardanza
        valor_esperado = sueldoBasico + bonificacionMovilidad + bonificacionSuplementaria + pagoHorasExtras - (descuentoFaltas + descuentoTardanzas)

        self.assertEqual(resultado, valor_esperado)

if __name__ == '__main__':
    unittest.main()

